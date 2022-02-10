# noinspection PyUnresolvedReferences
from flask import Blueprint

todos_blueprint = Blueprint("todos", __name__, template_folder="templates")
