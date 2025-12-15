import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vicky@2017"
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE alx_book_store")
    print("Database 'alx_book_store' created successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")
