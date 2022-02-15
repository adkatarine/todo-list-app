from todolist.infra.sqlalchemy.models.todos import Todo
from todolist import db


class RepositoryTodo:
    """Classe CRUD dos dados da todolist no database."""

    def create(self, description: str, user_id: int):
        """Insere uma nova task no database.

        :param description: descrição da task
        :param user_id: id do usuário
        :return: Todo
        """
        todo = Todo(description=description, user_id=user_id)
        db.session.add(todo)
        db.session.commit()
        return todo

    def read(self, user_id: int):
        """Retorna todas as tasks cadastradas de um usuário.

        :param user_id: id do usuário
        :return: Todo
        """
        todos: Todo = Todo.query.filter_by(user_id=user_id).all()
        return todos

    def update(self, id: int, description: str):
        """Atualiza a descrição de uma task.

        :param id: id da task
        :param description: descrição atualizada da task
        :return: Todo
        """
        todo: Todo = Todo.query.filter_by(id=id).first()
        todo.description = description
        db.session.commit()

    def delete(self, id: int):
        """Exclui uma task do database.

        :param id: id da task
        :return: None
        """
        todo: Todo = Todo.query.filter_by(id=id).first()
        db.session.delete(todo)
        db.session.commit()

    def update_status(self, id: int):
        """Atualiza o status da task em True ou False.

        :param id: id da task
        :return: None
        """
        todo: Todo = Todo.query.filter_by(id=id).first()
        todo.status = not todo.status
        db.session.commit()
