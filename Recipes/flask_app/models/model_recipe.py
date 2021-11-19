from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import model_user

from flask import flash

import re

from flask_app import app

DATABASE = "recipe"

class Recipes:
    def __init__(self,data):
        self.id = data['id']
        self.instructions = data['instructions']
        self.description = data['description']
        self.name = data['name']
        self.under_30 = data ['under_30']
        self.date_made = data ['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = model_user.User.get_by_id({'id': data['user_id']})

    @classmethod
    def create(cls,data):
        query= "INSERT INTO recipes (instructions, description, name, user_id, under_30, date_made) VALUES (%(instructions)s, %(description)s, %(name)s, %(user_id)s, %(under_30)s, %(date_made)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []
        for row in results:
            recipes.append(cls(row))
        return recipes

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) <1:
            return False
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET instructions=%(instructions)s, description=%(description)s, name=%(name)s, number_of_sasquatches= %(number_of_sasquatches)s WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate(post_data):
        is_valid = True
        if len(post_data['instructions']) < 1:
            flash('instructions is required')
            is_valid = False
        if len(post_data['description']) < 1:
            flash('Description is required')
            is_valid = False
        if len(post_data['name']) < 1:
            flash('Name is required')
            is_valid = False
        if len(post_data['date_made']) < 1:
            flash('Date Made is required')
            is_valid = False

        return is_valid