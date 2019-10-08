from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField, HiddenField


class FileForm(FlaskForm):
    file = FileField(validators=[FileRequired()], label=HiddenField)
    submit = SubmitField('Import File')
