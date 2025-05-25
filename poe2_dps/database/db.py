import psycopg2
from config import config

def connect():
    connection = None
    try:
        params = config()
        print('connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params)

        #create a cursor to allow the execution of SQL commands in order to get results from databse
        crsr = connection.cursor()
        print('postgreSQL database version: ')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Databse connection terminated')
if __name__ == "__main__":
    connect()
