from http import HTTPStatus
from functools import wraps
from flask import request, g
import jwt
from app import db
from models.user import UserModel
from config.environment import SECRET


def secure_route(route_func):

    @wraps(route_func)
    def wrapper(*args, **kwargs):

        raw_token = request.headers.get("Authorization")
        print("line 16")

        if not raw_token:
            return {"message": "Unauthorised test 1"}, HTTPStatus.UNAUTHORIZED

        token = raw_token.replace("Bearer ", "")
        print("line 22")

        try:
            payload = jwt.decode(token, SECRET, "HS256")
            print("line 26")

            user_id = payload["sub"]
            print("line 29")

            user = db.session.query(UserModel).get(user_id)
            print("line 32")

            g.current_user = user
            print("line 35")

            return route_func(*args, **kwargs)

        except jwt.ExpiredSignatureError:
            return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED
        except Exception as e:
            print(e)
            return {"message": "Unauthorised on secure_route"}, HTTPStatus.UNAUTHORIZED

    return wrapper
