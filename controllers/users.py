# TO-DO: Get rid of any instances of print()

from datetime import datetime, timezone, timedelta
import jwt
from flask import Blueprint, request
from app import db
from config.environment import SECRET
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


@router.route("/login", methods=["POST"])
def log_in():
    user_dictionary = request.json
    user = db.session.query(UserModel).filter_by(email=user_dictionary["email"]).first()

    if not user:
        print("Email doesn't exist on the database.")
        return {"message": "Login failed. Please try again."}

    if not user.validate_password(user_dictionary["password"]):
        print("Wrong password.")
        return {"message": "Login failed. Please try again."}

    payload = {
        "exp": datetime.now(timezone.utc) + timedelta(days=1),
        "iat": datetime.now(timezone.utc),
        "sub": user.id,
    }

    token = jwt.encode(payload, SECRET, algorithm="HS256")

    return {"message": "Login successful!", "token": token}
