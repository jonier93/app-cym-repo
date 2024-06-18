import pymysql

db_host = 'instance-cym.c3c6wae6wjt0.us-east-2.rds.amazonaws.com'
db_user = 'jonier'
db_password = '12345678'
db_database = 'db_cym'
db_table = 'users'

def connectionSQL():
    try:
        connection_sql = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_database
        )
        print("Successfull connection to the database")
        return connection_sql
    except:
        print("Error connecting to the database")
        return None
    
def add_user(id, name, lastname, birthday):
    instruction_sql = "INSERT INTO " + db_table + " (id, name, lastname, birthday) VALUES ("+id+", '"+name+"', '"+lastname+"', '"+birthday+"')"
    connection_sql = connectionSQL()
    try:
        if connection_sql != None:
            cursor = connection_sql.cursor()
            cursor.execute(instruction_sql)
            connection_sql.commit()
            print("User added")
        else:
            print("Error connecting to the database")
    except Exception as err:
        print(err)