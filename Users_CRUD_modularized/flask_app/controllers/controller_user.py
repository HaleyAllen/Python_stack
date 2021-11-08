from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_user

@app.route('/')
def read_all():
    all_users = model_user.User.get_all()
    return render_template('index.html', all_users = all_users)

@app.route('/new/user')
def new_user():
    return render_template('create.html')

@app.route('/create/user', methods=['POST'])
def create_user():
    model_user.User.create(request.form)
    return redirect('/')

@app.route('/user/<int:id>')
def user_info(id):
    users = model_user.User.get_one({'id': id})
    return render_template('info.html', users = users)

@app.route('/edit/<int:id>')
def edit_user(id):
    users = model_user.User.get_one({'id': id})
    return render_template('edit.html', users= users)

@app.route('/edit/processing/<int:id>', methods=['POST'])
def edit_processing(id):
    data = {
        **request.form,
        'id':id
    }
    model_user.User.update(data)
    return redirect(f'/user/{id}')

@app.route('/delete/<int:id>')
def delete_user(id):
    model_user.User.delete({'id':id})
    return redirect ('/')