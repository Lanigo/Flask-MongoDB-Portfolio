import sys
from flask import Flask, Blueprint, render_template, request, flash
from forms import ContactForm
from flask.ext.mail import Message, Mail

website = Blueprint("website",__name__,template_folder="templates")

mail = Mail()

app = Flask(__name__)

app.secret_key = "development key"

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "lanigouws@gmail.com"
app.config["MAIL_PASSWORD"] = "eendvogelvleyoud"

mail.init_app(app)

@website.route("/")
def home():
    return render_template('home.html')
	
@website.route("/about")
def about():
	return render_template('about.html')
	
@website.route("/projects")
def projects():
	return render_template('projects.html')

@website.route("/contact", methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	
	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required')
			return render_template('contact.html', form=form)
		else:
			msg = Message(form.subject.data, sender='contacts@example.com', recipients=['lanigouws@gmail.com'])
			msg.body = """
			From: %s <%s>
			%s
			""" % (form.name.data, form.email.data, form.message.data)
			mail.send(msg)
			
			return render_template('contact.html', success=True)
			
	elif request.method == 'GET':
		return render_template('contact.html', form=form)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', debug=True)