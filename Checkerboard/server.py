from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html", num1=8, num2=8, color1="cornflowerblue", color2="blueviolet")

@app.route('/<int:num1>')
def checkerboardX(num1):
    return render_template("index.html", num1=num1, num2=8, color1="cornflowerblue", color2="blueviolet")

@app.route('/<int:num1>/<int:num2>')
def checkerboardXY(num1, num2):
    return render_template("index.html", num1=num1, num2=num2, color1="cornflowerblue", color2="blueviolet")

@app.route('/<int:num1>/<int:num2>/<string:color1>/')
def checkerboardXYC1(num1, num2, color1):
    return render_template("index.html", num1=num1, num2=num2, color1=color1, color2="blueviolet")

@app.route('/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
def checkerboardXYC1C2(num1, num2, color1, color2):
    return render_template("index.html", num1=num1, num2=num2, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)

