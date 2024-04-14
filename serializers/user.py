from marshmallow import fields
from app import marsh
from models.user import UserModel


class UserSerializer(marsh.SQLAlchemyAutoSchema):

    # TO-DO: password

    class Meta:
        model = UserModel
        load_instance = True
        load_only = ("email", "password", "password_hash")

