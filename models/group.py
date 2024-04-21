from app import db
from models.base import BaseModel
from models.group_category import GroupCategoryModel
from models.user import UserModel


class GroupModel(db.Model, BaseModel):

    __tablename__ = "groups"

    name = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)
    brief_desc = db.Column(db.Text, nullable=False)
    contact_name = db.Column(db.Text, nullable=False)
    contact_number = db.Column(db.Text, nullable=False)
    full_desc = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    categories = db.relationship(
        "GroupCategoryModel", back_populates="group")

    user = db.relationship("UserModel", back_populates="group")
