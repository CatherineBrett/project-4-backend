from http import HTTPStatus
from marshmallow.exceptions import ValidationError
from flask import Blueprint, request, g
from models.group import GroupModel
from models.category import CategoryModel
from models.group_category import GroupCategoryModel
from app import db
from middleware.secure_route import secure_route
from serializers.group import GroupSerializer
from serializers.category import CategorySerializer
from serializers.group_category import GroupCategorySerializer

group_serializer = GroupSerializer()
category_serializer = CategorySerializer()
group_category_serializer = GroupCategorySerializer()


router = Blueprint("groups", __name__)


@router.route("/groups", methods=["GET"])
def get_all_groups():
    groups = db.session.query(GroupModel).all()
    return group_serializer.jsonify(groups, many=True)


@router.route("/groups/<int:group_id>", methods=["GET"])
def get_single_group(group_id):
    group = db.session.query(GroupModel).get(group_id)

    if not group:
        return {"message": "Group not found."}, HTTPStatus.NOT_FOUND

    return group_serializer.jsonify(group)


@router.route("/groups", methods=["POST"])
@secure_route
def create_group():
    group_dictionary = request.json

    try:
        categories_list = group_dictionary["categories"]
        del group_dictionary["categories"]
        group_dictionary["user_id"] = g.current_user.id
        group_model = group_serializer.load(group_dictionary)
        group_model.save()

        for category in categories_list:
            req_category = (
                db.session.query(CategoryModel).filter_by(name=category).first()
            )
            group_category_model = GroupCategoryModel(
                group_id=group_model.id, category_id=req_category.id
            )
            group_category_model.save()

        return group_serializer.jsonify(group_model)

    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR


@router.route("/groups/<int:group_id>", methods=["PUT"])
@secure_route
def update_group(group_id):

    try:
        group_to_update = db.session.query(GroupModel).get(group_id)

        if not group_to_update:
            return {"message": "Group not found"}, HTTPStatus.NOT_FOUND

        if group_to_update.user_id != g.current_user.id:
            return {
                "message": "You are not authorised to edit this group"
            }, HTTPStatus.UNAUTHORIZED

        group_dictionary = request.json

        categories_list = group_dictionary["categories"]
        del group_dictionary["categories"]

        group = group_serializer.load(
            group_dictionary, instance=group_to_update, partial=True
        )

        group.save()

        original_categories = db.session.query(GroupCategoryModel).filter_by(
            group_id=group_to_update.id
        )
        original_categories.delete()

        for category in categories_list:
            req_category = (
                db.session.query(CategoryModel).filter_by(name=category).first()
            )
            group_category_model = GroupCategoryModel(
                group_id=group_to_update.id, category_id=req_category.id
            )
            group_category_model.save()

        return group_serializer.jsonify(group)

    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR


@router.route("/groups/<int:group_id>", methods=["DELETE"])
@secure_route
def delete_group(group_id):

    try:
        group_to_delete = db.session.query(GroupModel).get(group_id)

        if not group_to_delete:
            return {"message": "Group not found"}, HTTPStatus.NOT_FOUND

        if (
            group_to_delete.user_id == g.current_user.id
            or g.current_user.username == "adminuser"
        ):
            groups_categories_to_delete = db.session.query(
                GroupCategoryModel
            ).filter_by(group_id=group_to_delete.id)
            groups_categories_to_delete.delete()

            group_to_delete.remove()
            return "", HTTPStatus.NO_CONTENT

        return {
            "message": "You are not authorised to delete this group"
        }, HTTPStatus.UNAUTHORIZED

    except Exception as e:
        print(e)
        return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR
