from flask_app import app

from flask import render_template, request, redirect, session

from flask_app.models import model_user
from flask_app.models import model_recipe


@app.route('/dashboard')
def dashboard():
    if "uuid" not in session:
        return redirect('/')

    return render_template(
        'dashboard.html',
        user = model_user.User.get_by_id({"id":session['uuid']}),
        all_recipes = model_recipe.Recipes.get_all()
    )

@app.route('/new/recipe')
def new_recipe():
    return render_template('new_recipe.html',user = model_user.User.get_by_id({"id":session['uuid']}))

@app.route('/create/recipe', methods = ['POST'])
def create_recipe():
    if not model_recipe.Recipes.validate(request.form):
        return redirect('/new/recipe')
    data = {
        **request.form,
        "user_id": session["uuid"]
    }

    model_recipe.Recipes.create(data)
    
    return redirect('/dashboard')

@app.route('/recipe/<int:id>')
def view_recipe(id):
    return render_template(
        'recipe.html',
        user = model_user.User.get_by_id({"id":session['uuid']}),
        recipe = model_recipe.Recipes.get_one({'id':id})
    )

@app.route('/recipe/<int:id>/edit')
def edit_recipe(id):
    return render_template(
        'edit_recipe.html',
        recipe = model_recipe.Recipes.get_one({'id':id})
    )

@app.route('/recipe/<int:id>/update', methods=["POST"])
def update_recipe(id):
    if not model_recipe.Recipes.validate(request.form):
        return redirect (f'/recipe/{id}/edit')
    data = {
        **request.form,
        'id': id
    }
    model_recipe.Recipes.update(data)
    return redirect ('/dashboard')

@app.route('/recipe/<int:id>/delete')
def delete_recipe(id):
    model_recipe.Recipes.delete({'id':id})
    return redirect('/dashboard')
