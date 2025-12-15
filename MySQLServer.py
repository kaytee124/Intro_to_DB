from mysql.connector import connect

mydb = connect(
    host="localhost",
    user="root",
    password= "Vicky@2017",
)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
print("Database 'alx_book_store' created successfully.")