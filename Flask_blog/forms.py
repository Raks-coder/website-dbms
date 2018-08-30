from flask_wtf import FlaskForm
from wtforms import StringFeild,PasswordFeild,SubmitFeild,BooleanFeild
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
	username=StringFeild('Username',validators=
		[DataRequired(),
		Length(min=2,max=20)])
	email=StringFeild('email',validators=[DataRequired(),Email()])
	password=PasswordFeild('password',validators=[DataRequired()])
	confirm_password=PasswordFeild('Confirm password',validators=[DataRequired(),EqualTo('password')])
	submit=SubmitFeild('Sign Up')



class LoginForm(FlaskForm):
	email=StringFeild('email',validators=[DataRequired(),Email()])
	password=PasswordFeild('password',validators=[DataRequired()])
	remember=BooleanFeild('Remember me')
	submit=SubmitFeild('Login ')
