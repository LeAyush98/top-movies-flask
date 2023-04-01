from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired
from wtforms.widgets import TextArea, SubmitInput

class AddMovieForm(FlaskForm):
    name = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField("Add Movie", widget=SubmitInput(), render_kw={"style": "background-color: #B8621B; color: white;"})