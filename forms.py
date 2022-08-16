from wtforms import Form, StringField
from wtforms.validators import InputRequired

class CommentForm(Form):
     user = StringField('user',validators=[InputRequired("Este campo es obligatorio")])
     passwd = StringField('passwd',validators=[InputRequired("Este campo es obligatorio")])