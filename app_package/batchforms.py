from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateTimeField, DateField, SelectField
from wtforms.validators import DataRequired, EqualTo
import datetime

class AddBatchForm(FlaskForm):
    batch_name=StringField("Batch Name: ",validators=[DataRequired()])
    date=datetime.datetime.today()
    start_date = DateTimeField("Start Date",default=date.today())
    end_date = DateTimeField("End Date",default=date.today())
    course_name=SelectField("Course Name : ",choices=[('java','java'),('spring boot','spring boot'),('python','python')])
    status=SelectField("Status : ",choices=[('Active','Active'),('Inactive','Inactive')])
    submit=SubmitField("Add Batch")

class ModifyBatchForm(FlaskForm):
    date=datetime.datetime.today()
    start_date=DateTimeField("Start Date",default=date.today())
    end_date=DateTimeField("End Date",default=date.today())
    status=SelectField("Status : ",choices=[('Active','Active'),('Inactive','Inactive')])
    submit=SubmitField("Modify Batch")


        