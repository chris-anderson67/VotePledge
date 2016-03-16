from flask import Flask

app = Flask(__name__)

# make sure that hellow is associated with app
# route to root (/) 
@app.route("/")
def hello():
    return "Hellow World!"

@app.route("/about")
def about_page():
    return "This is a web page."

@app.route("/sayhi/<name>")
def sayhi_page(name):
    return "Hi, " + name


if __name__ == "__main__":
    app.run(host="0.0.0.0")
