from app import marsh
from models.category import CategoryModel


class CategorySerializer(marsh.SQLAlchemyAutoSchema):

    class Meta:
        model = CategoryModel
        load_instance = True
