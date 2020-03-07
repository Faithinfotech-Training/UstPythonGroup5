from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FloatField,RadioField,IntegerField,TextAreaField

from wtforms.validators import DataRequired,EqualTo,ValidationError







class AddCourseForm(FlaskForm):
    
    coursename=StringField("CourseName: ",validators=[DataRequired(message="invalid data")])
    duration=IntegerField("Duration:(in weeks)" ,validators=[DataRequired(message="invalid data")])
    coursefees=FloatField("Fees: ",validators=[DataRequired(message="invalid data")])  
    
    status=RadioField("type:",choices=[('active','active'),('inactive','inactive')])
    description=TextAreaField("Description:(in weeks)" ,validators=[DataRequired(message="invalid data")])
    submit=SubmitField("New Course")
class ModifyCourseForm(FlaskForm):
    id=IntegerField("Id of the Course  to be modified: ")
   
    duration=IntegerField("Duration:(in weeks)")
    coursefees=FloatField("Fees: ") 
    
    status=RadioField("type:",choices=[('active','active'),('inactive','inactive')])
    description=TextAreaField("Description:") 
    
    submit=SubmitField("Modify course")
