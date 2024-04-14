from marshmallow import fields
from app import marsh
from models.group_category import GroupCategoryModel


class GroupCategorySerializer(marsh.SQLAlchemyAutoSchema):

    category = fields.Nested("CategorySerializer")

    class Meta:
        include_fk = True
        model = GroupCategoryModel
        load_instance = True
