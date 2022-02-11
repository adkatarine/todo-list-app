from todolist import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<Email {self.email}>"
