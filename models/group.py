from app import db

# TO-DO: Import UserModel


class GroupModel(db.Model):

    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False)
    brief_desc = db.Column(db.Text, nullable=False)
    category_one = db.Column(db.Text, nullable=False)
    category_two = db.Column(db.Text, nullable=True)
    category_three = db.Column(db.Text, nullable=True)
    contact_name = db.Column(db.Text, nullable=False)
    contact_number = db.Column(db.Text, nullable=False)
    full_desc = db.Column(db.Text, nullable=False)

    # TO-DO: UserModel

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("UserModel", backref="groups")
