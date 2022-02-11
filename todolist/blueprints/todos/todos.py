# noinspection PyUnresolvedReferences
from flask import Blueprint, render_template


todos_blueprint = Blueprint("todos", __name__, template_folder="templates")


@todos_blueprint.route("/todolist", methods=["GET"])
def todolist():
    return render_template("todolist.html")
