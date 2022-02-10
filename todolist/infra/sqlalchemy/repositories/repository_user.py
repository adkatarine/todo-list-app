from todolist.infra.sqlalchemy.models.models import User
from todolist import db


class RepositoryUser:
    def create(self, name: str, email: str, password: str):
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
