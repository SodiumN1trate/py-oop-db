import mysql.connector

database = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="first_db"
)


cursor = database.cursor()