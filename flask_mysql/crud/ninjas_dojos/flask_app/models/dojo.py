from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO dojos (name, created_at, updated_at)
        VALUES (%(name)s, NOW(), NOW());
        """
        dojo_id = connectToMySQL("dojos_and_ninjas_flask").query_db(query, data)
        return dojo_id

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas_flask").query_db(query)

        all_dojos = []
        for row in results:
            all_dojos.append(cls(row))
        return all_dojos

    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"

        results = connectToMySQL("dojos_and_ninjas_flask").query_db(query, data)
        one_dojo = cls(results[0])
        for row in results:
            row_data = {
                "id" : row["ninjas.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age" :row["age"],
                "created_at" : row["ninjas.created_at"],
                "updated_at" : row["ninjas.updated_at"]
            }
            one_dojo.ninjas.append(ninja.Ninja(row_data))
        return one_dojo


