from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["generic"]
user_record = db["user"]

