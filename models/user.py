from sqlalchemy.ext.hybrid import hybrid_property
from app import db, bcrypt
from models.base import BaseModel


class UserModel(db.Model, BaseModel):

    __tablename__ = "users"

    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password_hash = db.Column(db.Text, nullable=True)

    group = db.relationship("GroupModel", back_populates="user")

    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self, plaintext_pw):
        encoded_pw = bcrypt.generate_password_hash(plaintext_pw)
        self.password_hash = encoded_pw.decode("utf-8")

    def validate_password(self, login_pw):
        return bcrypt.check_password_hash(self.password_hash, login_pw)
