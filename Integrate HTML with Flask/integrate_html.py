from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = request.form['science']
        maths = request.form['maths']
        history = request.form['history']
        total_score = (int(science) + int(maths) + int(history))/3
        return redirect(url_for('validate',score=total_score))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/validate/<int:score>')
def validate(score):
    res = ""
    if score < 60:
        res = "Failed"
    else:
        res = "Passed"
    return render_template("results.html", score=score,result=res)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
