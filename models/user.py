from app import db

from models.base import BaseModel


class UserModel(db.Model, BaseModel):

    __tablename__ = "users"

    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=True)

    group = db.relationship("GroupModel", back_populates="user")
