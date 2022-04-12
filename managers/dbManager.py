import mysql.connector

def initDb():
    return  mysql.connector.connect(host="remotemysql.com", user="1x1a8MMUSv", password="kvAt89FidK", port="3306", database="1x1a8MMUSv")

def getConnection():
    try:
        return initDb()
    except Exception as ex:
        print("error. ex: %s" % (ex))

def executeNonQuery(sql : str):
    try:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
    except Exception as ex:
        print("error. ex: %s" % (ex))
        connection.rollback()

def executeSelectQuery(sql : str, fetchOne = False):
    try:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(sql)
        return cursor.fetchOne() if fetchOne else cursor.fetchall();
        
    except Exception as ex:
        print("error. ex: %s" % (ex))
        connection.rollback()
