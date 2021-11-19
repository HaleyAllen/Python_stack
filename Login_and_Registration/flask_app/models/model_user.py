from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

import re

from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

DATABASE = "login_registration"

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_user(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for row in results:
            users.append(User(row))
        return users

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) <1:
            return False
        return User(results[0])

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) <1:
            return False
        return User(results[0])

    @classmethod
    def create_user(cls,data):
        query ="INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, now(),now())"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_register(post_data):
        is_valid = True # we assume this is true
        if len(post_data['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(post_data['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']): 
            flash("Invalid email address!")
            is_valid=False
        else:
            user = User.get_by_email({"email":post_data['email']})
            if user:
                flash('An account exists with that email already!')
                is_valid = False
        if len(post_data['password']) < 8:
            flash('Password must be at least 8 characters.')
            is_valid = False
        if post_data['password'] != post_data['confirm_password']:
            flash('Password and Confirm Password must match.')
            is_valid = False
        return is_valid
        

    @staticmethod
    def validate_login(post_data):
        user = User.get_by_email({"email":post_data["email"]})
        if not user:
            flash('Invalid Cridentials')
            return False
        if not bcrypt.check_password_hash(user.password, post_data['password']):
            flash('Invalid Password')
            return False
        return True