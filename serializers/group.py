from marshmallow import fields
from app import marsh
from models.group import GroupModel
from serializers.user import UserSerializer


class GroupSerializer(marsh.SQLAlchemyAutoSchema):

    categories = fields.Nested("GroupCategorySerializer", many=True)
    # Adding the following but not sure about it - remove it if something breaks!
    # user = fields.Nested("UserSerializer", many=False)

    class Meta:
        model = GroupModel
        load_instance = True
        # Might not need this now I've nested the user??
        include_fk = True
