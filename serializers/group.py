from marshmallow import fields
from app import marsh
from models.group import GroupModel
from serializers.user import UserSerializer


class GroupSerializer(marsh.SQLAlchemyAutoSchema):

    categories = fields.Nested("GroupCategorySerializer", many=True)

    class Meta:
        model = GroupModel
        load_instance = True
        include_fk = True
