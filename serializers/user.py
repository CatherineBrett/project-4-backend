import re
from marshmallow import fields, ValidationError
from app import marsh
from models.user import UserModel


def validate_password_reqs(password):
    if len(password) < 10:
        raise ValidationError("Your password must be at least 10 characters long")
    elif re.search("[A-Z]", password) is None:
        raise ValidationError("Your password must include a capital letter")


class UserSerializer(marsh.SQLAlchemyAutoSchema):

    password = fields.String(required=True, validate=validate_password_reqs)

    class Meta:
        model = UserModel
        load_instance = True
        load_only = ("email", "password", "password_hash")
