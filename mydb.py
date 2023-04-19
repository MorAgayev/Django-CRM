import mysql.connector

# Define out dataBase
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'moraga3112',

)


# Prepare a cursor object 
cursorObject = dataBase.cursor()


# Create a DB
cursorObject.execute("CREATE DATABASE dcrmDB")

print('DB created sucssesfulys')