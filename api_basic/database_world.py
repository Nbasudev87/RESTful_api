import mysql.connector
from mysql.connector import Error
import time


try:
    db_connection = mysql.connector.connect(user='root', password='Nbasudev87@',
                              host='localhost',
                              database='world')
    cursor = db_connection.cursor(dictionary=True)
    qury_data='select ID,Name,CountryCode,District,Population from city where CountryCode="NLD";'
    #cursor.execute('select ID,Name,CountryCode,District,Population from city;')
    cursor.execute(qury_data)
    records=cursor.fetchall()
    print(type(records))
    #for item in records:
        #print(item)
    #names = [row[0] for row in cursor.fetchall()]
    #for (ID,Name,CountryCode,District,Population) in records:
        #print("{},\t\t{},\t\t{},\t\t{},\t\t{}".format(ID,Name,CountryCode,District,Population))
    print("prinding records")

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (db_connection.is_connected()):
        db_connection.close()
        cursor.close()
        print("MySQL connection is closed")

