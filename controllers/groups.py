from flask import Blueprint
from models.group import GroupModel
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
