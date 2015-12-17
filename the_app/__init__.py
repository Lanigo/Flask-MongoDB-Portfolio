from flask import Flask, render_template, request, flash
from website.views import website
from blog.views import posts
from website.forms import ContactForm
from flask.ext.mail import Message, Mail
from blog.admin import admin
from markdown import markdown
from flask import Markup

mail = Mail()

app = Flask(__name__)

app.register_blueprint(website,url_prefix="/")
app.register_blueprint(posts,url_prefix="/posts")
app.register_blueprint(admin,url_prefix="/admin")

app.secret_key = "development key"

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "lanigouws@gmail.com"
app.config["MAIL_PASSWORD"] = "LeeGordonMcKillop1968"

mail.init_app(app)

@app.route("/")
def index():
	return render_template("layout.html")
	
@app.route("/home")
def home():
	return render_template("home.html")
	
@app.route("/about")
def about():
	return render_template("about.html")
	
@app.route("/projects")
def projects():
	return render_template('projects.html')
	
@app.route("/contact", methods=['GET', 'POST'])
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
	
@app.route("/posts")
def posts():
	return render_template("base.html")
	
@app.route("/admin")
def admin():
	return render_template("admin/base.html")
	
@app.template_filter("markdown")
def render_markdown(markdown_text):
    return Markup(markdown(markdown_text))
