from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



app = Flask(__name__)

# Scurity key 
app.config["SECRET_KEY"] = "a secure key dont puch git"

# Create a Form Class

class NamerForm(FlaskForm):
    name = StringField("Wahts your Name", validators=[DataRequired()])
    submit = SubmitField("submit")



# create name page

@app.route("/name", methods = ["GET", "POST"])
def name():
    name = None
    form = NamerForm()
    # validate Form /data
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""

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


if __name__ == "__main__":
    app.run(debug=True)


















# save code on git hub version controle

# git add .
# git commit -am "what did i change?"
# git push






