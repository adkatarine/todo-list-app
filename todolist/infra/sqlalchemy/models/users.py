from todolist import db, login_manager
from werkzeug.security import generate_password_hash

# noinspection PyUnresolvedReferences
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id: int):
    return User.query.filter_by(id=user_id).first()


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f"<Email {self.email}>"
