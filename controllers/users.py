from flask import Blueprint, request
from models.user import UserModel
from serializers.user import UserSerializer


user_serializer = UserSerializer()

router = Blueprint("users", __name__)


@router.route("/signup", methods=["POST"])
def sign_up():
    user_dictionary = request.json
    user = user_serializer.load(user_dictionary)
    user.save()
    return user_serializer.jsonify(user)


# TO-DO: Finish this (needs password validation and token etc.)
@router.route("/login", methods=["POST"])
def log_in():
    user_dictionary = request.json
