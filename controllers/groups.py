from flask import Blueprint, request
from models.group import GroupModel
from models.category import CategoryModel
from serializers.group import GroupSerializer
from serializers.category import CategorySerializer
from serializers.group_category import GroupCategorySerializer

group_serializer = GroupSerializer()
category_serializer = CategorySerializer()
group_category_serializer = GroupCategorySerializer()


router = Blueprint("groups", __name__)


@router.route("/groups", methods=["GET"])
def get_all_groups():
    groups = GroupModel.query.all()
    return group_serializer.jsonify(groups, many=True)


@router.route("/groups/<int:group_id>", methods=["GET"])
def get_single_group(group_id):
    group = GroupModel.query.get(group_id)
    return group_serializer.jsonify(group)


@router.route("/groups", methods=["POST"])
def create_group():
    group_dictionary = request.json
    # TO-DO: update this hardcoded user ID once you've done your secure route:
    group_dictionary["user_id"] = 1
    # TO-DO: figure out what to do about categories
    group = group_serializer.load(group_dictionary)
    group.save()
    return group_serializer.jsonify(group)


# TO-DO: Permissions
@router.route("/groups/<int:group_id>", methods=["PUT"])
def update_group(group_id):
    group_dictionary = request.json
    group_to_update = GroupModel.query.get(group_id)

    group = group_serializer.load(
        group_dictionary, instance=group_to_update, partial=True
    )

    group.save()
    return group_serializer.jsonify(group)


# TO-DO: Permissions
@router.route("/groups/<int:group_id>", methods=["DELETE"])
def delete_group(group_id):
    group = GroupModel.query.get(group_id)
    group.remove()
    return ""
