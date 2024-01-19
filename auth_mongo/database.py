from pymongo import MongoClient


# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")


def database(db_name: str, collection: str):
    """This function creates and returns a tuple of mongodb and a collection"""
    db = client[db_name]
    collection = db[collection]

    return db, collection



db, collection  = database("people", "user" )
