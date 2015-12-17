from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email
from wtforms.fields.html5 import EmailField

class ContactForm(Form):
	name = TextField("Name", validators=[InputRequired("Please enter your name.")])
	email = EmailField("Email", validators=[InputRequired("Please enter your email address."), Email("Please enter your email address.")])
	subject = TextField("Subject", validators=[InputRequired("Please enter a subject.")])
	message = TextAreaField("Message", validators=[InputRequired("Please enter a message.")])
	submit = SubmitField("Send")
	
 