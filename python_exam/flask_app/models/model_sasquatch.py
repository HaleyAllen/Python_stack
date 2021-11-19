from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import model_user

from flask import flash

import re

from flask_app import app

DATABASE = "sasquatch_sightings"

class Sightings:
    def __init__(self,data):
        self.id = data['id']
        self.location = data['location']
        self.what_happened = data['what_happened']
        self.date_sighted = data['date_sighted']
        self.number_of_sasquatches = data['number_of_sasquatches']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users = model_user.User.get_by_id({'id': data['users_id']})

    @classmethod
    def create(cls,data):
        query= "INSERT INTO sasquatch_sightings (location, what_happened, date_sighted, number_of_sasquatches, users_id) VALUES (%(location)s, %(what_happened)s, %(date_sighted)s, %(number_of_sasquatches)s, %(users_id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sasquatch_sightings;"
        results = connectToMySQL(DATABASE).query_db(query)
        sasquatch_sightings = []
        for row in results:
            sasquatch_sightings.append(cls(row))
        return sasquatch_sightings

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM sasquatch_sightings WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) <1:
            return False
        return cls(results[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE sasquatch_sightings SET location=%(location)s, what_happened=%(what_happened)s, date_sighted=%(date_sighted)s, number_of_sasquatches= %(number_of_sasquatches)s WHERE id=%(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM sasquatch_sightings WHERE id = %(id)s"
        connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validate(post_data):
        is_valid = True
        if len(post_data['location']) < 1:
            flash('Location is required')
            is_valid = False
        if len(post_data['what_happened']) < 1:
            flash('What Happened is required')
            is_valid = False
        if len(post_data['date_sighted']) < 1:
            flash('Date Sighted is required')
            is_valid = False
        if int(post_data['number_of_sasquatches']) < 1:
            flash('Number if sasquatches must be at least 1')
            is_valid = False

        return is_valid