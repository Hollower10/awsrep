
import pymysql

db_host = "database-1.c5cui28qcxx7.us-east-2.rds.amazonaws.com"
db_user = "diego"
db_password = "Hollower1."
db_database = "DB_USERS"

try: 
    pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )
    print("Succesfull connection to database")
except Exception as err:
    print("Error connecting to database:", err)