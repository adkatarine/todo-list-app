# noinspection PyUnresolvedReferences
from flask import Blueprint, render_template, request, redirect, url_for
from todolist.infra.sqlalchemy.repositories.repository_todo import RepositoryTodo

# noinspection PyUnresolvedReferences
from flask_login import current_user


todos_blueprint = Blueprint("todos", __name__, template_folder="templates")


@todos_blueprint.route("/todolist", methods=["GET"])
def todolist():
    todos = RepositoryTodo().read(user_id=current_user.id)
    return render_template("todolist.html", todos=todos)


@todos_blueprint.route("/create", methods=["POST"])
def create():
    print(f"ID USER: {current_user.id}")
    RepositoryTodo().create(
        description=request.form["description"], user_id=current_user.id
    )
    todos = RepositoryTodo().read(user_id=current_user.id)
    return redirect(url_for("todolist", todos=todos))


@todos_blueprint.route("/update", methods=["POST"])
def update():
    RepositoryTodo().update(
        id=request.form["id"], description=request.form["description"]
    )
    todos = RepositoryTodo().read(user_id=current_user.id)
    return redirect(url_for("todos.todolist", todos=todos))


@todos_blueprint.route("/remove/<int:id>", methods=["GET"])
def remove(id: int):
    RepositoryTodo().delete(id=id)
    todos = RepositoryTodo().read(user_id=current_user.id)
    return redirect(url_for("todos.todolist", todos=todos))
