from marshmallow import fields
from app import marsh
from models.user import UserModel


class UserSerializer(marsh.SQLAlchemyAutoSchema):

    password = fields.String(required=True)

    class Meta:
        model = UserModel
        load_instance = True
        load_only = ("email", "password", "password_hash")
