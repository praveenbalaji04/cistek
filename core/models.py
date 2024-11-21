from config import Config
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId


mongo_client = MongoClient(Config.MONGO_DB_URI)
database = mongo_client.get_database(Config.MONGO_DB_NAME)


class User:

    def __init__(self):
        self.collection = database.get_collection('user')

    def as_json(self, user_obj):
        user_obj["_id"] = str(user_obj["_id"])
        return user_obj

    def add_document(self, user_data):
        doc = self.collection.insert_one({
            "first_name": user_data.get('first_name'),
            "last_name": user_data.get('last_name'),
            "dob": user_data.get('dob'),
            "address": user_data.get('address'),
            "gender": user_data.get("gender"),
            "email": user_data.get('email'),
            "phone_number": user_data.get('phone_number'),
            "created_at": datetime.now().isoformat()
        })
        return doc.inserted_id

    def filter(self, query):
        cursor = self.collection.find(query)
        users_obj = []
        for user in cursor:
            self.as_json(user)
            users_obj.append(user)
        return users_obj

    def get_document(self, user_id):
        user_data = self.collection.find_one({"_id": ObjectId(user_id)})
        if user_data:
            return self.as_json(user_data)

    def get_document_by_name(self, first_name):
        return self.collection.find_one({"first_name": first_name})

    def update_document(self, user_id, user_data):
        return self.collection.update_one({"_id": ObjectId(user_id)}, {"$set": user_data})

    def delete_document(self, user_id):
        return self.collection.delete_one({"_id": ObjectId(user_id)})
