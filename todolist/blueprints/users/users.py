# noinspection PyUnresolvedReferences
from flask import Blueprint, render_template, redirect, url_for

# noinspection PyUnresolvedReferences
from flask_login import login_user, logout_user
from todolist.infra.sqlalchemy.repositories.repository_user import RepositoryUser
from todolist.infra.sqlalchemy.repositories.repository_todo import RepositoryTodo
from todolist.infra.forms.form_register import FormRegister
from todolist.infra.forms.form_login import FormLogin
from todolist.infra.sqlalchemy.verifications.verification_user import (
    verify_password,
    verify_emails_equals,
    verify_user_exists,
)


users_blueprint = Blueprint(
    "users",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/users/static",
)


@users_blueprint.route("/")
def index():
    return render_template("index.html")


@users_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = FormRegister()
    if form.validate_on_submit():
        if verify_user_exists(RepositoryUser().read(email=form.email.data)):
            RepositoryUser().create(
                name=form.name.data, email=form.email.data, password=form.password.data
            )
            return redirect(url_for("users.login"))
    return render_template("register.html", form=form)


@users_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        user = RepositoryUser().read(email=form.email.data)

        if verify_emails_equals(form.email, user):
            return redirect(url_for("users.login", form=form))
        elif verify_password(user.password, form.password.data):
            login_user(user)
            todos = RepositoryTodo().read(user.id)
            return redirect(url_for("todos.todolist", todos=todos))
    return render_template("login.html", form=form)


@users_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("users.index"))
