import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   connection = mysql.connector.connect(host='localhost',
                             database='utoronto',
                             user='phpmyadmin',
                             password='EQ$ua.12')
   sql_insert_query = """ INSERT INTO `small_data_test`
                          (`lat`, `lon`, `timestamp`, `session_dt`) VALUES ('-10.727808','25.384920','1554731777', NOW())"""
   cursor = connection.cursor()
   result  = cursor.execute(sql_insert_query)
   connection.commit()
   print ("Record inserted successfully into python_users table")
except mysql.connector.Error as error :
    connection.rollback() #rollback if any exception occured
    print("Failed inserting record into python_users table {}".format(error))
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
