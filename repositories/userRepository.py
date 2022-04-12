from managers import dbManager

def saveUser(user) :
    try :
        sql = f"INSERT INTO users (id, name, login, password) VALUES ('{user.id}', '{user.name}', '{user.login}', '{user.password}' )"
        dbManager.executeNonQuery(sql)
        
    except Exception as ex :
        print("error. ex: %s" % (ex))
        raise(ex)

def getUser(id) :
    try :
        sql = f"SELECT * FROM users WHERE id = '{id}'"
        return dbManager.executeSelectQuery(sql)
        
    except Exception as ex :
        print("error. ex: %s" % (ex))
        raise(ex)

def deleteUser(id) :
    try :
        sql = f"DELETE FROM users WHERE id = '{id}'"
        dbManager.executeNonQuery(sql)
        
    except Exception as ex :
        print("error. ex: %s" % (ex))
        raise(ex)