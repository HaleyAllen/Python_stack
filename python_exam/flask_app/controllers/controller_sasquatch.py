from flask_app import app

from flask import render_template, request, redirect, session

from flask_app.models import model_user
from flask_app.models import model_sasquatch


@app.route('/dashboard')
def dashboard():
    if "uuid" not in session:
        return redirect('/')

    return render_template(
        'dashboard.html',
        user = model_user.User.get_by_id({"id":session['uuid']}),
        all_sightings = model_sasquatch.Sightings.get_all()
    )

@app.route('/new/sighting')
def new_sighting():
    return render_template('new_sasquatch.html',user = model_user.User.get_by_id({"id":session['uuid']}))

@app.route('/create/sighting', methods = ['POST'])
def create_sighting():
    if not model_sasquatch.Sightings.validate(request.form):
        return redirect('/new/sighting')
    data = {
        **request.form,
        "users_id": session["uuid"]
    }

    model_sasquatch.Sightings.create(data)
    
    return redirect('/dashboard')

@app.route('/sighting/<int:id>')
def view_sighting(id):
    return render_template(
        'sighting.html',
        user = model_user.User.get_by_id({"id":session['uuid']}),
        sighting = model_sasquatch.Sightings.get_one({'id':id})
    )

@app.route('/sighting/<int:id>/edit')
def edit_sighting(id):
    return render_template(
        'edit_sighting.html',
        user = model_user.User.get_by_id({"id":session['uuid']}),
        sighting = model_sasquatch.Sightings.get_one({'id':id})
    )

@app.route('/sighting/<int:id>/update', methods=["POST"])
def update_sighting(id):
    if not model_sasquatch.Sightings.validate(request.form):
        return redirect (f'/sighting/{id}/edit')
    data = {
        **request.form,
        'id': id
    }
    model_sasquatch.Sightings.update(data)
    return redirect ('/dashboard')

@app.route('/sighting/<int:id>/delete')
def delete_sighting(id):
    model_sasquatch.Sightings.delete({'id':id})
    return redirect('/dashboard')
