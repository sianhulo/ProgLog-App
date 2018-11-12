from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email    = StringField('Email', [Email(),
                                     InputRequired(message='¿Olvidaste tu email?')])
    password = PasswordField('Password', [InputRequired(message='Debe colocar la contraseña.')])

class SignupForm(FlaskForm):
    email    = StringField('Email', [Email(),
                                     InputRequired(message='¿Olvidaste tu email?')])
    password = PasswordField('Password', [InputRequired(message='Debe colocar la contraseña.')])
    confirm  = PasswordField('Confirm Password', [EqualTo('password', message="Las contraseñas no coinciden."),
                                                  InputRequired(message='Debe colocar la contraseña.')])
    name     = StringField('Name', [InputRequired(message="Debe colocar un nombre.")])
