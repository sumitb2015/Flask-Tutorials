from flask import Flask

#WSGI application - connect with webserver and web application
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! " \
           "This is Sumit Bandyopadhyay .Please visit http://127.0.0.1:5000" \
           "and please subscribe my channel"

@app.route("/members")
def welcome_members():
    return ("Welcome Members to my Youtube Channel")

if __name__ == "__main__":
    app.run(debug=True)