# noinspection PyUnresolvedReferences
from flask import Blueprint, render_template, redirect, url_for
from todolist.infra.sqlalchemy.repositories.repository_user import RepositoryUser
from todolist.infra.forms.form_register import FormRegister


users_blueprint = Blueprint("users", __name__, template_folder="templates")


@users_blueprint.route("/")
def index():
    return render_template("index.html")


@users_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = FormRegister()
    if form.validate_on_submit():
        RepositoryUser().create(
            name=form.name.data, email=form.email.data, password=form.password.data
        )
        redirect(url_for("login"))
    return render_template("register.html", form=form)


@users_blueprint.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@users_blueprint.route("/logout")
def logout():
    return render_template("index.html")
