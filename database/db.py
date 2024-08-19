
import pymysql

db_host = "database-1.c5cui28qcxx7.us-east-2.rds.amazonaws.com"
db_user = "diego"
db_password = "Hollower1."
db_database = "DB_USERS"

def conection_sql():
    try: 
        objetosql=pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
         )
        print("Succesfull connection to database")
        return objetosql
    except Exception as err:
        print("Error connecting to database:", err)
        return None

def insert_register(id, name, lastname, birthday):
    instruccion = "INSERT INTO USERS(id, name, lastname, birthday) VALUES("+id+", '"+name+"', '"+lastname+"', '"+birthday+"')"
    objetosql=conection_sql()
    cursor=objetosql.cursor()
    try:
        cursor.execute(instruccion)
        objetosql.commit()
        print("registrado")
    except Exception as err:
        print("error usuario",err)
