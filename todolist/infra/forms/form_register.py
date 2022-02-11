# noinspection PyUnresolvedReferences
from flask_wtf import FlaskForm

# noinspection PyUnresolvedReferences
from wtforms import StringField, PasswordField

# noinspection PyUnresolvedReferences
from wtforms.validators import DataRequired


class FormRegister(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
