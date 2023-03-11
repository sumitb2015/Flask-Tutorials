from flask import Flask,render_template,request,redirect,url_for
'''
Here to use the templates, we need to place the html files in the templates folder 
This is because python will look for the html files in the templates folder 
'''
app = Flask(__name__,template_folder="./templates")

'''
Templating engine for Flask
{%...%} for statement
{{statement}} statement to print output
{{#...#} comments
'''
@app.route('/sucess/<int:score>')
def success(score):
    return "The person has passed the exam and the score is {}".format(score)

@app.route('/failed/<int:score>')
def failed(score):
    return "The person has failed the exam and the score is {}".format(score)

# In below code,the int:marks is a variable which is passed to the template
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks >= 60:
        result = "success"
    else:
        result = "failed"
    return render_template('results.html',result=marks)
    # return redirect(url_for(result,score=marks))

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)