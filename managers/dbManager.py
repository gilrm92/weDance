from pymongo import MongoClient

CONNECTION_STRING = "mongodb://gilrm:Gilbertorm92@wedance-shard-00-00.ylapw.mongodb.net:27017,wedance-shard-00-01.ylapw.mongodb.net:27017,wedance-shard-00-02.ylapw.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-cycfhh-shard-0&authSource=admin&retryWrites=true&w=majority"
client = MongoClient(CONNECTION_STRING)
weDanceDB = client["weDance"]
userCollection = weDanceDB["users"]

def saveUser(user) :
    try :
        userCollection.insert_one(user.__dict__)
        
    except Exception as ex :
        print("error. ex: %s" % (ex))
        raise(ex)

def getUser(id) :
    try :
        return userCollection.find_one({"id": id},  {'_id': 0})
        
    except Exception as ex :
        print("error. ex: %s" % (ex))
        raise(ex)

def deleteUser(id) :
    try :
        userCollection.delete_one( {"id": id} )
        
    except Exception as ex :
        print("error. ex: %s" % (ex))
        raise(ex)