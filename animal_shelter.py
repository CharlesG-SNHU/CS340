from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        """
        Inserts a document into the animals collection.
        return True if insert was acknowledged, otherwise False
        """
        if data is not None:
            result = self.database.animals.insert_one(data)
            return True if result.acknowledged else False
        else:
            raise Exception("Data parameter is empty")

    def read(self, query):
        """
        Queries documents in the animals collection.
        return list of matching documents, an empty list if none found or error
        """
        if query is not None:
            results = list(self.database.animals.find(query, {"_id": False}))
            return results
        else:
            return []
        
    def update(self, lookup, update_data):
        """
        Queries for and updates document(s) in the animals collection.
        """
        if lookup is None or update_data is None:
            raise Exception("Lookup query and update data must not be None")

        result = self.database.animals.update_many(lookup, update_data)
        return result.modified_count
    
    def delete(self, lookup):
        """
        Queries for and removes document(s) from the animals collection.
        """
        if lookup is None:
            raise Exception("Lookup query must not be None")
        result = self.database.animals.delete_many(lookup)
        return result.deleted_count