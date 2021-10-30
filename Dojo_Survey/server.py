from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template("index.html")

@app.route('/reset')
def reset():
    return render_template("submitted.html")

if __name__=="__main__":
    app.run(debug=True)