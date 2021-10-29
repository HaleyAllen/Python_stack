
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/play')
def onlyThree():
    return render_template("index.html", times=3, color="aqua")

@app.route('/play/<int:times>')
def howMany(times):
    return render_template("index.html", times=times, color="aqua")

@app.route('/play/<int:num>/<color>')
def changeColor(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)

