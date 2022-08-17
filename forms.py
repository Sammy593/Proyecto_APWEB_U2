from wtforms import Form, StringField
from wtforms.validators import DataRequired

class CommentForm(Form):
     user = StringField('user',validators=[DataRequired("Este campo es obligatorio")])
     passwd = StringField('passwd',validators=[DataRequired("Este campo es obligatorio")])