from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, Email, EqualTo

class LoginForm(FlaskForm):
    email    = TextField('Email', [Email(),
                                   Required(message='¿Olvidaste tu email?')])
    password = PasswordField('Password', [
                                   Required(message='Debe colocar la contraseña.')])
