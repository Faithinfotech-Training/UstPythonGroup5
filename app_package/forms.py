from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField , IntegerField ,RadioField
from wtforms.validators import Email
from wtforms.validators import DataRequired, EqualTo, ValidationError
from wtforms.fields.html5 import EmailField
from app_package.models import Role,Login,Registration

class LoginForm(FlaskForm):
    username=StringField("Username: ",validators=[DataRequired()])
    password=PasswordField("Password: ", validators=[DataRequired()])
    remember_me=BooleanField("Remember Me")
    submit=SubmitField("Sign in")
    


class RegistrationForm(FlaskForm):
    fullname=StringField("FULLNAME: ",validators=[DataRequired()])
    username=StringField("USERNAME: ",validators=[DataRequired()])
    mobile=IntegerField("MOBILE :",validators=[DataRequired()])
    email=StringField("Email:",validators=[DataRequired(),Email()])
    role_id=RadioField('', choices = [('1','admin'),('2','cordinator')],validators=[DataRequired()])
    password=PasswordField("PASSWORD: ", validators=[DataRequired()])
    password2=PasswordField("REPEAT PASSWORD: ",validators=[DataRequired(),EqualTo("password")])
    submit=SubmitField("REGISTER")
    


       