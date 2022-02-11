from todolist.infra.sqlalchemy.models.users import User
from todolist import db, login_manager


@login_manager.user_loader
def get_user(user_id: int):
    return User.query.filter_by(id=user_id).first()


class RepositoryUser:
    def create(self, name: str, email: str, password: str) -> User:
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    def read(self, email: str) -> User:
        user: User = User.query.filter_by(email=email).first()
        return user

    def update(self):
        pass

    def delete(self):
        pass
