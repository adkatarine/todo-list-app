from todolist.infra.sqlalchemy.models.todos import Todo
from todolist import db


class RepositoryTodo:
    def create(self, description: str, user_id: int):
        todo = Todo(description=description, user_id=user_id)
        db.session.add(todo)
        db.session.commit()
        return todo

    def read(self, user_id: int):
        todos: Todo = Todo.query.filter_by(user_id=user_id).all()
        return todos

    def update(self, id: int, description: str):
        todo: Todo = Todo.query.filter_by(id=id).first()
        todo.description = description
        db.session.commit()

    def delete(self, id: int):
        todo: Todo = Todo.query.filter_by(id=id).first()
        db.session.delete(todo)
        db.session.commit()

    def update_status(self, id: int):
        todo: Todo = Todo.query.filter_by(id=id).first()
        todo.status = not todo.status
        db.session.commit()
