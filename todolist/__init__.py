# noinspection PyUnresolvedReferences
from flask import Flask, request

# noinspection PyUnresolvedReferences
from flask_sqlalchemy import SQLAlchemy

# noinspection PyUnresolvedReferences
from flask_migrate import Migrate

# from todolist.blueprints.todos.todos import todos_blueprint

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///storage.db"
app.config.from_object("config")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from todolist.infra.sqlalchemy.models.users import User

from todolist.blueprints.users.users import users_blueprint

app.register_blueprint(users_blueprint)
# app.register_blueprint(todos_blueprint)
