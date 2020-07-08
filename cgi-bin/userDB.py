from pymongo import MongoClient
from collections import OrderedDict
import sys

'''
    Creates User Database in MongoDB
    Sets up Validation rules in createUserDB()
    Insertion is done in insertUser()
    Deletion is done deleteUser()
'''

#Connection to MongoDB
uri = ""
client = MongoClient(uri) 
db = client.testX #TODO Change Cluster Name

#Deletes collection
def resetUserDB():
    db.accounts.drop()

#Inserts new account that adhere to Schema
def createUserDB():
    db.create_collection("accounts")

    #Schema
    #https://docs.mongodb.com/manual/reference/operator/query/jsonSchema/#op._S_jsonSchema
    vexpr = {
        "$jsonSchema":{
            "bsonType": "object",
            "required": [ "name", "username", "password", "group", "organization" ],
            "properties": {
                "name": {
                "bsonType": "string",
                "description": "First Name and Last Name. Must be a string and is required"
                },
                "username": {
                "bsonType": "string",
                "description": "Login Credential. Must be a string and is required"
                },
                "password": {
                "bsonType": "string",
                "description": "Login Credential. Must be a string and is required"
                },
                "group": {
                "enum": [ "ADMIN", "INSTRUCTOR", "USER", None],
                "description": "Can only be one of the enum values and is required"
                },
                "organization": {
                "bsonType": "string",
                "description": "Must be a string and is required"
                }
            }
        }
    }

    #Applies Validation
    cmd = OrderedDict([('collMod', 'accounts'),
            ('validator', vexpr),
            ('validationLevel', 'moderate')])

    db.command(cmd)

#Inserts new account ensuring no duplicates
def insertUser(name, usr, pwd, grp, org):
    try:
        query = {
            "name":name, 
            "username":usr, 
            "password":pwd, 
            "group":grp, 
            "organization":org
        }

        #Check for duplicate, create new if unique
        db.accounts.update(query, query, True)
        print("All good.")
    except:
        print("exc:", sys.exc_info())


#Delete account by name
def deleteUser(name):
    try:
        query = {
            "name":name
        }

        #Check for duplicate, create new if unique
        db.accounts.delete_one(query)
        print("All good.")
    except:
        print("exc:", sys.exc_info())

'''TODO Various Update Methods that Seem Fit'''

#Usage
# insertUser("Natty B", "test", "tst", "ADMIN", "WEBER")
# deleteUser("Natty B")