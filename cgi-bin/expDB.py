from pymongo import MongoClient
from collections import OrderedDict
import sys

'''
    Creates Experiment Database in MongoDB
    Sets up Validation rules in createExpDB()
    Insertion is done in insertExp()
    Deletion is done in deleteExp()
'''

#Connection to MongoDB
uri = "mongodb+srv://root:toor@cluster0-qbeba.mongodb.net/<dbname>?retryWrites=true&w=majority"
client = MongoClient(uri) 
db = client.testX #TODO Change Cluster Name

#Deletes collection
def resetExpDB():
    db.experiments.drop()

#Inserts new experiment that adhere to Schema
def createExpDB():
    db.create_collection("experiments")

    #Schema
    #https://docs.mongodb.com/manual/reference/operator/query/jsonSchema/#op._S_jsonSchema
    vexpr = {
        "$jsonSchema":{
            "bsonType": "object",
            "required": [ "experiment", "facilitator", "antenna", "fileLocation", "visibility" ], #TODO
            "properties": {
                "experiment": {
                    "bsonType": "string",
                    "description": "Must be a string and is required"
                },
                "facilitator": {
                    "bsonType": "string", #"object",
                    "description": "Must be a User in Database"
                },
                "antenna": {
                    "enum": [ "YAGI", None],
                    "description": "Can only be one of the enum values and is required"
                },
                "fileLocation": {
                    "bsonType": "string",
                    "description": "Must be a string and is required"
                },
                "config": { #TODO
                    "bsonType": "string",
                    "description": "Must be a string and is required"
                },
                "media": { #TODO
                    "bsonType": "string",
                    "description": "Must be a string and is required"
                },
                "visibility": {
                    "enum": [ "PUBLIC", "Private", None],
                    "description": "Can only be one of the enum values and is required"
                },
            }
        }
    }

    #Applies Validation
    cmd = OrderedDict([('collMod', 'experiments'),
            ('validator', vexpr),
            ('validationLevel', 'moderate')])

    db.command(cmd)

#Inserts new account ensuring no duplicates
def insertExp(exp, usr, ant, fl, vis):
    try:
        query = {
            "experiment": exp,
            "facilitator": usr, 
            "antenna": ant,
            "fileLocation": fl, 
            "visibility": vis
            # config
            # media
        }

        #Check for duplicate, create new if unique
        db.experiments.update(query, query, True)
        print("All good.")
    except:
        print("exc:", sys.exc_info())


#Delete account by name
def deleteExp(name):
    try:
        query = {
            "experiment":name
        }

        #Check for duplicate, create new if unique
        db.experiments.delete_one(query)
        print("All good.")
    except:
        print("exc:", sys.exc_info())

'''TODO Various Update Methods that Seem Fit'''

#Usage
resetExpDB()
createExpDB()
insertExp("LOVELACE", "test", "YAGI", "ADMIN", "PUBLIC")
# deleteExp("LOVELACE")