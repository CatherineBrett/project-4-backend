from app import db
from models.base import BaseModel
from models.category import CategoryModel


class GroupCategoryModel(db.Model, BaseModel):

    __tablename__ = "groups_categories"

    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    group = db.relationship(
        "GroupModel", back_populates="categories", cascade="all, delete"
    )
    category = db.relationship(
        "CategoryModel", back_populates="groups", cascade="all, delete"
    )
