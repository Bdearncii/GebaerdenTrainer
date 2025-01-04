import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost", # host?
        user="admin",
        password="4Cgebaerden",
        database="gebaerdentrainer"
    )