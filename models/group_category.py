from app import db
from models.base import BaseModel


class GroupCategoryModel(db.Model, BaseModel):

    __tablename__ = "groups_categories"

    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    group = db.relationship("GroupCategoryModel", back_populates="categories")
    category = db.relationship("GroupCategoryModel", back_populates="groups")
