# noinspection PyUnresolvedReferences
from flask import Blueprint, render_template, redirect, url_for

# noinspection PyUnresolvedReferences
from flask_login import login_user, logout_user
from todolist.infra.sqlalchemy.repositories.repository_user import RepositoryUser
from todolist.infra.forms.form_register import FormRegister
from todolist.infra.forms.form_login import FormLogin
from todolist.infra.sqlalchemy.verifications.verification_user import verify_password


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
    form = FormLogin()
    if form.validate_on_submit():
        user = RepositoryUser().read(email=form.email.data)
        print(user.email)

        if user and verify_password(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("todos.todolist"))

    return render_template("login.html", form=form)


@users_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
