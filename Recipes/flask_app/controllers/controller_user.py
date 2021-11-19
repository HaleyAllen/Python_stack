from flask_app import app

from flask import render_template, request, redirect, session

from flask_app.models import model_user

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def read_all():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
    if not model_user.User.validate_login(request.form):
        return redirect('/')
    user = model_user.User.get_by_email({"email": request.form["email"]})
    session['uuid'] = user.id
    return redirect('/dashboard')

@app.route('/register', methods=['POST'])
def register():
    if not model_user.User.validate_register(request.form):
        return redirect('/')
    hash_pass = bcrypt.generate_password_hash(request.form['password'])
    data={
        **request.form,
        'password': hash_pass
    }
    user_id = model_user.User.create_user(data)
    session['uuid'] = user_id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


