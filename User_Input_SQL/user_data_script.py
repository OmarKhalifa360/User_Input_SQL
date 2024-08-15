import os
import json
from datetime import datetime

file_name = "user_data.txt"
current_month = datetime.now().month
current_year = datetime.now().year

'''
In case of not using a in open(), a = "append"
'''
cwd = os.getcwd()
directory = os.path.join(cwd, os.path.dirname(__file__))
answer_directory = os.path.join(directory, file_name)



def id_check(file_path, id_name):
    if os.path.exists(file_path):
        with open(file_path, 'r') as c:
            return str(id_name) in c.read()
    return False

def info_write(fname):
    global first_name, last_name, age, gender, year_of_birth, id_name

    with open(fname, 'a') as f:
        
        print("Welcome to our demo version of signup registration")
        
        try:
            
            first_name = input("Please enter your first name: ")
            
            if first_name.isalpha():
                pass
            else:
                print("First Name Must Be Alphabetic (Unless you're Elon's son). Please Try Again")
                return info_write(fname)
            
            last_name = input("Please enter your last name: ")
            
            if last_name.isalpha():
                pass
            else:
                print("Last Name Must Be Alphabetic (Unless your dad is Elon's son). Please Try Again")
                return info_write(fname)
            
            age = int(input('Please enter your age: ').strip())

            if age > 0:
                pass
            else:
                print('Age not available. Please Try Again')
                return info_write(fname)

            gender = input("Please enter your gender (Male/Female/Other): ").upper()
            
            if gender == "MALE" or gender == "FEMALE" or gender == "OTHER":
                pass
            else:
                print("Invalid Gender, Please Try Again.")
                return info_write(fname)
            
            year_of_birth = int(input('Please enter your year of birth: ').strip())
            age_from_now = (current_year + (current_month / 12)) - year_of_birth

            if len(str(year_of_birth)) == 4 and age_from_now > 18 and int(age_from_now) == age:
                pass
            else:
                print("Please ensure that you entered the correct year of birth or you're over 18 y/o")
                return info_write(fname)

            id_name = str(input("Please enter your id (It should be 3 numbers): "))
            user_data = {}

            if len(str(id_name)) == 3 and str(id_name).isalnum():
                if id_check(answer_directory, id_name):
                    print("ID already exists. Cannot enter the data.")
                    return info_write(fname)
                else:
                    data_string = {
                                    "First Name": first_name, 
                                    "Last Name": last_name,
                                    "Gender": gender
                                    }
                
                    user_data[id_name] = data_string

                    f.write(str(user_data))
                    f.write("\n")
            else:
                print("Your id should be consisted of 3 numbers only. Please Try Again")
                return info_write(fname)
        
        except ValueError as v:
            print(v)
            print("Something went wrong. Please Try Again")
            return info_write(fname)
        
        f.close()


info_write(answer_directory)

###############################################################################################
import pyodbc

conn = None
cursor = None

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

    # SQL Insert Query
    insert_query = """
    INSERT INTO Users (user_id, first_name, last_name, age, gender, year_of_birth)
    VALUES (?, ?, ?, ?, ?, ?)
    """

    # Executing the query with user data
    cursor.execute(insert_query, (id_name, first_name, last_name, age, gender, year_of_birth))

    # Commit the transaction
    conn.commit()

except pyodbc.Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    if cursor is not None:
        cursor.close()
    if conn is not None :
        conn.close()
