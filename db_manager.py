import sys
import mysql.connector
import config
from queries import db_queries


class MYSQL_CONNECTOR:
    def __init__(self):
        self.CONNECTON = None
        self.QUERIES = db_queries
        self.HOST = config.db_host
        self.USER = config.db_user
        self.PASSWORD = config.db_password
        self.DB_NAME = config.db_name
    def connector(self, host, user, password, database):
        try:
            connection = mysql.connector.connect(host=host,
                                            user=user,
                                            password=password,
                                            database=database)
            if (connection.is_connected()):
                print("Success mysql connection!")
                return connection

        except mysql.connector.Error as connection_error:
            print(connection_error)
            sys.exit(1)

    def run_mysql_query(self, query):
        try:
            self.CONNECTON = self.connector(self.HOST, self.USER, self.PASSWORD, self.DB_NAME)
            cursor = self.CONNECTON.cursor()
            cursor.execute(query)
            self.CONNECTON.commit()
            print("Query works successfully!")
        except mysql.connector.errors.DatabaseError as database_error:
            print(database_error)
            sys.exit(1)

def main():
    connector = MYSQL_CONNECTOR()
    for query  in connector.QUERIES:
        connector.run_mysql_query(connector.QUERIES[query])
    
    if (connector.CONNECTON.is_connected()):
        connector.CONNECTON.close()
        print("MySQL connection is closed")
        sys.exit(1)

if __name__ == '__main__':
    main()
    
