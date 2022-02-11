from todolist.infra.sqlalchemy.models.todos import Todo
from todolist import db


class RepositoryTodo:
    def create(self, description: str, user_id: int):
        todo = Todo(description=description, user_id=user_id)
        db.session.add(todo)
        db.session.commit()

    def read(self, id_user: int):
        todos: Todo = Todo.query.filter_by(id_user=id_user).all()
        return todos

    def update(self, id: int, description: str):
        todo: Todo = Todo.query.filter_by(id=id).first()
        todo.description = description
        db.session.commit()

    def delete(self, id: int):
        todo: Todo = Todo.query.filter_by(id=id).first()
        db.session.delete(todo)
        db.session.commit()
