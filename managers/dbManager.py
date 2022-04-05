from pymongo import MongoClient

CONNECTION_STRING = "mongodb://localhost:27017"
client = MongoClient(CONNECTION_STRING)
weDanceDB = client["weDance"]
userCollection = weDanceDB["users"]

def saveUser(user) :
    try :
        userCollection.insert_one(user.__dict__)
        
    except Exception as ex :
        print("error when adding. ex: %s" % (ex))

def getUser(id) :
    try :
        return userCollection.find_one({"_id": id})
        
    except Exception as ex :
        print("error when adding. ex: %s" % (ex))

def deleteUser(id) :
    try :
        userCollection.delete_one( {"_id": id} )
        
    except Exception as ex :
        print("error when adding. ex: %s" % (ex))