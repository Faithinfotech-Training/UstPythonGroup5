from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, EqualTo,NumberRange

class AddResourceForm(FlaskForm):
    res_name=StringField("Resource name: ",validators=[DataRequired()])
    res_capacity=IntegerField("Capacity: ",validators=[DataRequired(),NumberRange(min=1)])
    res_status=RadioField("Resource status: ",choices=[('available','available'),('not available','not available')])
    res_rent=IntegerField("Resource rent: ",validators=[DataRequired(), NumberRange(min=1)])
    type_of_use=SelectField("Type of use : ",choices=[('seminar','seminar'),('workshop','workshop'),('training','training')])
    submit=SubmitField("Create new resource")
    
class UpdateResourceForm(FlaskForm):
    res_capacity=IntegerField("new capacity: ",validators=[DataRequired(),NumberRange(min=1)])
    res_status=RadioField("Resource status: ",choices=[('available','available'),('not available','not available')])
    res_rent=IntegerField("Enter the rent : ",validators=[DataRequired(),NumberRange(min=1)])
    type_of_use=SelectField("Type of use : ",choices=[('seminar','seminar'),('workshop','workshop'),('training','training')])
    submit=SubmitField("update")
    
        