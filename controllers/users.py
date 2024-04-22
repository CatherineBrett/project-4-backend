from datetime import datetime, timezone, timedelta
from http import HTTPStatus
import jwt
from flask import Blueprint, request, g
from marshmallow.exceptions import ValidationError
from app import db
from config.environment import SECRET
from models.user import UserModel
from models.group import GroupModel
from models.group_category import GroupCategoryModel
from middleware.secure_route import secure_route
from serializers.user import UserSerializer


user_serializer = UserSerializer()

router = Blueprint("users", __name__)


@router.route("/user", methods=["GET"])
@secure_route
def get_current_user():
    return user_serializer.jsonify(g.current_user)


@router.route("/signup", methods=["POST"])
def sign_up():

    try:
        user_dictionary = request.json

        if user_dictionary["password"] != user_dictionary["password_confirmation"]:
            return {
                "errors": "Passwords do not match",
                "message": "Passwords do not match",
            }, HTTPStatus.UNPROCESSABLE_ENTITY

        del user_dictionary["password_confirmation"]

        username_taken = (
            db.session.query(UserModel)
            .filter_by(username=user_dictionary["username"])
            .first()
        )

        if username_taken:
            return {"message": "Username not available"}, HTTPStatus.CONFLICT

        user_model = user_serializer.load(user_dictionary)

        user_model.save()
        return user_serializer.jsonify(user_model)

    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong - please try again",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        return {
            "message": "Something went wrong - please try again"
        }, HTTPStatus.INTERNAL_SERVER_ERROR


@router.route("/login", methods=["POST"])
def log_in():

    try:
        user_dictionary = request.json

        user = (
            db.session.query(UserModel)
            .filter_by(email=user_dictionary["email"])
            .first()
        )

        if not user:
            return {
                "message": "Login failed. Please try again."
            }, HTTPStatus.UNAUTHORIZED

        if not user.validate_password(user_dictionary["password"]):
            return {
                "message": "Login failed. Please try again."
            }, HTTPStatus.UNAUTHORIZED

        payload = {
            "exp": datetime.now(timezone.utc) + timedelta(days=1),
            "iat": datetime.now(timezone.utc),
            "sub": user.id,
        }

        token = jwt.encode(payload, SECRET, algorithm="HS256")

        return {"message": "Login successful!", "token": token}

    except Exception as e:
        return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR


@router.route("/users/<int:user_id>", methods=["PUT"])
@secure_route
def update_user(user_id):

    try:
        user_to_update = db.session.query(UserModel).get(user_id)

        if not user_to_update:
            return {"message": "User not found"}, HTTPStatus.NOT_FOUND

        if user_to_update.id != g.current_user.id:
            return {
                "message": "You are not authorised to edit this account"
            }, HTTPStatus.UNAUTHORIZED

        user_dictionary = request.json

        user = user_serializer.load(
            user_dictionary, instance=user_to_update, partial=True
        )

        user.save()

        return user_serializer.jsonify(user)

    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR


@router.route("/users/<int:user_id>", methods=["DELETE"])
@secure_route
def delete_user(user_id):

    try:
        user_to_delete = db.session.query(UserModel).get(user_id)

        if not user_to_delete:
            return {"message": "User not found"}, HTTPStatus.NOT_FOUND

        if user_to_delete.id != g.current_user.id:
            return {
                "message": "You are not authorised to delete this account"
            }, HTTPStatus.UNAUTHORIZED

        groups_to_delete = db.session.query(GroupModel).filter_by(
            user_id=user_to_delete.id
        )

        for group in groups_to_delete:
            groups_categories_to_delete = db.session.query(
                GroupCategoryModel
            ).filter_by(group_id=group.id)
            groups_categories_to_delete.delete()

        groups_to_delete.delete()

        user_to_delete.remove()
        return "", HTTPStatus.NO_CONTENT

    except Exception as e:
        return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR
