from flask import Flask, render_template, url_for


app = Flask(__name__)


# user a variable called name localhos:port/test/lorenz will have a resulte
@app.route("/test/<name>")
def username(name):
    return "<h1>How are you {}?????</h1>".format(name)

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
# Ivalid Server Error thing
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)


# save code on git hub version controle

# git add .
# git commit -am "what did i change?"
#
