# In case of Different authentication than Windows Authentication

import pymysql

def verify_mysql_connection(host, user, password, database):
    try:
        # Attempt to establish a connection to the MySQL server
        conn = pymysql.connect(
            host=host, # Enter your server name
            user=user, # Enter your username
            password=password, # Enter your password
            database='UserDatabase'
        )
        print("Connection successful!")

        # Close the connection
        conn.close()

    except pymysql.err.OperationalError as e:
        print("OperationalError:", e)
        # Error numbers and messages can provide more details on what might be wrong
        if e.args[0] == 1045:
            print("Invalid user name or password. Please check your credentials.")
        elif e.args[0] == 2003:
            print("Can't connect to MySQL server. Ensure the server is running and reachable.")
        elif e.args[0] == 1049:
            print("Unknown database. Please check the database name.")
        else:
            print("An operational error occurred. Details:", e)

    except pymysql.err.InternalError as e:
        print("InternalError:", e)
        # Additional handling for internal errors

    except Exception as e:
        print("An unexpected error occurred:", e)

# Example usage
host = "localhost"
user = "root"
password = "toor$St0r3"
database = "UserDatabase"

verify_mysql_connection(host, user, password, database)
################################################################################
# In case of using Windows Authentication
import pyodbc

# Define the connection string
connection_string = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=UserDatabase;"
    "Trusted_Connection=yes;"
)

try:
    # Establishing a connection to the database
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")

    # Create a cursor object
    cursor = conn.cursor()

    # Perform database operations using cursor
    # Example: Execute a query
    cursor.execute("SELECT * FROM Users")

    # Fetch results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print("Error:", e)
