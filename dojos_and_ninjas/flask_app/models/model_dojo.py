from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = 'dojos_and_ninjas'

class Ninjas:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos_id = data['dojos_id']

    @classmethod

    def get_ninjas(cls, data:dict):
        query = "SELECT * FROM ninjas WHERE dojos_id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def create_ninjas(cls, data:dict):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojos_id) VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

# -----------------------DOJO----------------------------------------------------------------------#

class Dojos:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for user in results:
            dojos.append(cls(user))
        return dojos

    @classmethod
    def get_dojo(cls, data:dict):
        query = "SELECT * FROM dojos WHERE id= %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])
    @classmethod
    def create_dojos(cls, data:dict):
        query = "INSERT INTO dojos (name) VALUES(%(name)s)"
        return connectToMySQL(DATABASE).query_db(query, data)


