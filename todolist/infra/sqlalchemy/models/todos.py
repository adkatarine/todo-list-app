from todolist import db


class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    user = db.relationship("User", foreign_keys=user_id)

    def __init__(self, description: str, user_id: int):
        self.description = description
        self.status = False
        self.user_id = user_id

    def __repr__(self):
        return f"<Todo {self.id}>"
