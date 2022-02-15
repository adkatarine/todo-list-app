# noinspection PyUnresolvedReferences
from flask_wtf import FlaskForm

# noinspection PyUnresolvedReferences
from wtforms import StringField, PasswordField

# noinspection PyUnresolvedReferences
from wtforms.validators import DataRequired


class FormLogin(FlaskForm):
    """Classe utilizada para gerenciar de forma mais fácil os dados de login recebidos
    de um formulário."""

    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
