#we connect with the mongoclient and create a database named darpgDB

import pymongo

def get_database():
 
   client = pymongo.MongoClient("mongodb://localhost:27017/")
 
   return client['darpgDB']
