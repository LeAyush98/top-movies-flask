from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired
from wtforms.widgets import TextArea, SubmitInput

class MovieForm(FlaskForm):
    rating = StringField('Your Rating out of 10', validators=[DataRequired()])
    review = TextAreaField('Your Review', validators=[InputRequired("Please enter a valid review!")], widget=TextArea())
    submit = SubmitField("Update", widget=SubmitInput(), render_kw={"style": "background-color: #B8621B; color: white;"})