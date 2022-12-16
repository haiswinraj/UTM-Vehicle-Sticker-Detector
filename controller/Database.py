import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="kali",
    database="usds",
    auth_plugin="mysql_native_password"
)
