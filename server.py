#import flask
# render_template digunakan untuk merender html dan css . 
# url_for is used in file layout.html to search css file
# flash is used to send alert within the web page
# redirect library is used to redirect to other page when the user complete the login fomr
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# TESSSSTT

class User(db.Model):
	# id set to primary key 

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable = False)
    email = db.Column(db.String(120), unique=True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)

	# backref is used to make additional column in Post database. 
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    # user.id . the U is not in uppercase , because it is referencing from
	# table name and column name
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

posts = [
	{
		"author" 		: "Ilham",
		"post_date" 	: "August 20, 2019",
		"content_title"	: "First post",
		"content"		: "lorem ipsum dolor si amet"
	},

	{
		"author" 		: "Adhim Mc",
		"post_date" 	: "July 12, 2019",
		"content_title"	: "Second post",
		"content"		: "lorem ipsum dolor si amet second"
	},

	{
		"author" 		: "ilhamm179",
		"post_date" 	: "March 18, 2019",
		"content_title"	: "Third post",
		"content"		: "lorem ipsum dolor si amet third"
	},
	
	{
		"author" 		: "TestUser",
		"post_date" 	: "July 20, 2019",
		"content_title"	: "Fourth post",
		"content"		: "lorem ipsum dolor si amet Fourth"
	}
]


@app.route("/")
@app.route("/home")
def home():
	return render_template('mainpage.html' , posts = posts)


@app.route("/about")
def about():
  return render_template('about.html') 

@app.route("/biodata")
def index():
    return jsonify(biodata)


@app.route("/register" , methods = ['GET','POST'])
def register():
  form = RegistrationForm()

  if form.validate_on_submit():
	# below Python 3.6 use this one :
	# flash('Account created for {}!'.format({form.username.data}))
  		flash(f'Account created for { form.username.data }! ' , 'success')
  		return redirect('home')
  # else :
  #		flash(f'Account cannot be created ! check registration rules correctly ' , 'danger')
  return render_template('register.html' , title='Register' , form = form)


@app.route("/login" , methods = ['GET','POST'])
def login():
  Loginform = LoginForm()

  if Loginform.validate_on_submit():
  		flash(f'You are signed in as { Loginform.username.data }! ' , 'success')
  		return redirect('home')
  
  return render_template('login.html' , title='Login' , Loginform = Loginform)



app.run()
