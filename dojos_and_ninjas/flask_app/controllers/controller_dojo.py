from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_dojo

@app.route('/')
@app.route('/dojos')
def read_all():
    all_dojos = model_dojo.Dojos.get_all()
    return render_template('dojos.html',all_dojos = all_dojos)

@app.route('/create/dojos', methods=["POST"])
def create_dojo():
    model_dojo.Dojos.create_dojos(request.form)
    return redirect('/dojos')

@app.route('/ninjas')
def new_ninjas():
    all_dojos = model_dojo.Dojos.get_all()
    return render_template('ninjas.html',all_dojos = all_dojos)

@app.route('/create/ninjas', methods=["POST"])
def create_ninja():
    model_dojo.Ninjas.create_ninjas(request.form)
    return redirect('/show/ninjas')

@app.route('/show/ninjas/<int:id>')
def show_ninjas(id):
    all_ninjas = model_dojo.Ninjas.get_ninjas({'id': id})
    dojo = model_dojo.Dojos.get_dojo({'id': id})
    return render_template('view.html', all_ninjas = all_ninjas, dojo = dojo)