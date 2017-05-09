from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class LoginForm(FlaskForm):
	username = StringField('username', validators=[InputRequired])
	password = PasswordField('password', validators=[InputRequired])
	remember = BooleanField('remember me')

class RegistrationForm(FlaskForm):
	username = StringField('username', validators=[InputRequired, Length(min=4, max=15)])
	password = PasswordField('password', validators=[InputRequired, Length(min=4, max=80)])
	email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])