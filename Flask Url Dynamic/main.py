from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the score is {}".format(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the score is {}".format(score)

@app.route('/results/<int:marks>')
def results(marks):
    results = ""
    if marks < 50:
        results = "fail"
    else:
        results = "success"
    return redirect(url_for(results,score=marks))


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=80)