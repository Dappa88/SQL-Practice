import psycopg2
from . import dotenv
from psycopg2.extras import RealDictCursor
# 
def Connect_db():
        
    while True:

        try:
            conn = psycopg2.connect(host=dotenv.Process.host, database=dotenv.Process.database, user=dotenv.Process.user,
                                    password=dotenv.Process.password,cursor_factory=RealDictCursor)
            # cursor = conn.cursor()
            print("Database connection was succesfull!")
            # cursor.execute("SELECT * FROM shippers")
            # record = cursor.fetchall()
            # print("recordingnow",record)
            return conn
        except Exception as error:
            print("Connecting to database failed")
            print("Error: ", error)
            time.sleep(2)