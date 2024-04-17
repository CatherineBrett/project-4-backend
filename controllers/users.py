# TO-DO: Get rid of any instances of print()

from datetime import datetime, timezone, timedelta
from http import HTTPStatus
import jwt
from flask import Blueprint, request
from app import db
from config.environment import SECRET
from models.user import UserModel
from serializers.user import UserSerializer


user_serializer = UserSerializer()

router = Blueprint("users", __name__)


@router.route("/signup", methods=["POST"])
def sign_up():
    user_dictionary = request.json

    if user_dictionary["password"] != user_dictionary["password_confirmation"]:
        return {
            "errors": "Passwords no not match",
            "messages": "Something went wrong",
        }, HTTPStatus.UNPROCESSABLE_ENTITY

    del user_dictionary["password_confirmation"]

    user = user_serializer.load(user_dictionary)
    user.save()
    return user_serializer.jsonify(user)


@router.route("/login", methods=["POST"])
def log_in():
    user_dictionary = request.json
    user = db.session.query(UserModel).filter_by(email=user_dictionary["email"]).first()

    if not user:
        print("Email doesn't exist on the database.")
        return {"message": "Login failed. Please try again."}

    if not user.validate_password(user_dictionary["password"]):
        print("Wrong password.")
        return {"message": "Login failed. Please try again."}

    payload = {
        "exp": datetime.now(timezone.utc) + timedelta(days=1),
        "iat": datetime.now(timezone.utc),
        "sub": user.id,
    }

    token = jwt.encode(payload, SECRET, algorithm="HS256")

    return {"message": "Login successful!", "token": token}


# TO-DO: Permissions
@router.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user_dictionary = request.json
    user_to_update = UserModel.query.get(user_id)

    user = user_serializer.load(user_dictionary, instance=user_to_update, partial=True)

    user.save()
    return user_serializer.jsonify(user)


# TO-DO: Permissions
@router.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = UserModel.query.get(user_id)
    user.remove()
    return ""
