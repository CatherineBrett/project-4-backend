from app import db
from models.base import BaseModel


class CategoryModel(db.Model, BaseModel):

    __tablename__ = "categories"

    name = db.Column(db.Text, nullable=False, unique=True)

    groups = db.relationship(
        "GroupCategoryModel", back_populates="category")
