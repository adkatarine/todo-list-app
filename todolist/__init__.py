# noinspection PyUnresolvedReferences
from flask import Flask, request

# noinspection PyUnresolvedReferences
from flask_sqlalchemy import SQLAlchemy

# noinspection PyUnresolvedReferences
from flask_migrate import Migrate

# noinspection PyUnresolvedReferences
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


from todolist.infra.sqlalchemy.models.users import User


from todolist.blueprints.users.users import users_blueprint
from todolist.blueprints.todos.todos import todos_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(todos_blueprint)
