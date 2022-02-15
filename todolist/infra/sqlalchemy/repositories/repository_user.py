from todolist.infra.sqlalchemy.models.users import User
from todolist import db


class RepositoryUser:
    """Classe CRUD dos dados de usuário no database."""

    def create(self, name: str, email: str, password: str) -> User:
        """Insere um novo usuário no database.

        :param name: nome do usuário
        :param email: email do usuário
        :param password: senha do usuário
        :return: User
        """
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    def read(self, email: str) -> User:
        """Retorna o usuário cadastrado de acordo com o email recebido.

        :param email: email do usuário
        :return: User
        """
        user: User = User.query.filter_by(email=email).first()
        return user
