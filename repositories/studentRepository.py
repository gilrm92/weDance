from managers import dbManager

def saveStudent(student) :
    try :
        sql = f"INSERT INTO students (id, name, age, cpf, email) VALUES ('{student.id}', '{student.name}', '{student.age}', '{student.cpf}', '{student.email}')"
        dbManager.executeNonQuery(sql)
        
    except Exception as ex :
        print("error. ex: %s" % (ex))
        raise(ex)

def getStudents() :
    try :
        sql = f"SELECT * FROM students"
        return dbManager.executeSelectQuery(sql)
        
    except Exception as ex :
        print("error. ex: %s" % (ex))
        raise(ex)
    
def getStudent(id) :
    try :
        sql = f"SELECT * FROM students WHERE id = '{id}'"
        return dbManager.executeSelectQuery(sql)
        
    except Exception as ex :
        print("error. ex: %s" % (ex))
        raise(ex)

def deleteStudent(id) :
    try :
        sql = f"DELETE FROM students WHERE id = '{id}'"
        dbManager.executeNonQuery(sql)
        
    except Exception as ex :
        print("error. ex: %s" % (ex))
        raise(ex)