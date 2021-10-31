from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep my secret'

@app.route('/')
def survey():
    return render_template("index.html")

@app.route('/submitted')
def surveyAnswers():

    return render_template("submitted.html")

@app.route('/submitted_process', methods=["POST"])
def surveyAnswers_process():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['description']=request.form['description']
    return redirect('/submitted')

if __name__=="__main__":
    app.run(debug=True)