from managers import dbManager

def getUser(login, password) :
    try :
        sql = f"SELECT * FROM users WHERE login = '{login}' AND password = '{password}'"
        return dbManager.executeSelectQuery(sql)
        
    except Exception as ex :
        print("error. ex: %s" % (ex))
        raise(ex)