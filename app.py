from flask import Flask, render_template, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate


app = Flask(__name__)

# Scurity key 
app.config["SECRET_KEY"] = "a secure key dont puch git"
# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webserver.db'
# Initialize The Database
db = SQLAlchemy(app)
# solve the problem with the create all comand/function or so
migrate = Migrate(app, db)
# Create Model 
# Corrected model class name (capitalized and singular)
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create A Strin
    def __repr__(self):
        return "<Name %r>" % self.name
    

# Create a Form Class for the databases

class NamerForm(FlaskForm):
    name = StringField("Wahts your Name", validators=[DataRequired()])
    submit = SubmitField("submit")

# Create a Useracout
class AddUserForm(FlaskForm):
    name = StringField("What's your name?", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    submit = SubmitField("submit")


# route for user creaton
@app.route("/user/add", methods=["GET", "POST"])
def adduser():
    name = None
    form = AddUserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ""
        form.email.data = ""
        flash("User added")
    our_users = Users.query.order_by(Users.date_added)
    return render_template("adduser.html", form=form, name=name, our_users=our_users)



@app.route("/name", methods = ["GET", "POST"])
def name():
    name = None
    form = NamerForm()
    # validate Form /data
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("Form Submitted Successfuly")

    return render_template("name.html", name=name, form=form)


# user a variable called name localhos:port/test/lorenz will have a resulte
@app.route("/test/<name>")
def username(name):
    return "<h1>How are you {}?????</h1>".format(name)

# normal route to a html doc
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/base")
def base():
    return render_template("base.html")


# Create Custom Error Pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
# Ivalid Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


















# save code on git hub version controle

# git add .
# git commit -am "what did i change?"
# git push






