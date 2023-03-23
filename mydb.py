# Install MySQL on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysqlclient


import mysql.connector

dataBase  = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'

)

# cursor Object
cursorObject = dataBase.cursor()

# create DB
cursorObject.execute("CREATE DATABASE CRM;")

print("Database Created")