#!/usr/bin/env python

import pymysql
from subprocess import Popen, PIPE, STDOUT

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='mydb')
cur = conn.cursor()

print("Attempting to create new database...")
try:
    cur.execute("CREATE DATABASE mydb2")
    print("Creating new database")
except Exception:
    print("Database already exists")
print()

# close connection just to be sure
cur.close()
conn.close()

print("Trying to copy old database to new database...")

#args1 = ["mysqldump", "-h", "localhost", "-P", "3306", "-u", "root", "-p", "mydb"]
#args2 = ["mysql", "-h", "localhost", "-P", "3306", "-u", "root", "-p", "mydb2"]

subprocess.Popen("mysql --skip-column-names -u root -p'azarbod98765' -e 'show databases;' | while read dbname; do if [ \"$dbname\" = \"azarbod\" ] ; then mysqldump --lock-all-tables -u root -p'azarbod98765' \"$dbname\" > \"$(date +%Y%m%d)-$dbname\".sql; fi done", shell=True)

#p1 = Popen(args1, stdout=PIPE, stderr=STDOUT)
#p2 = Popen(args1, stdin=p1.stdout, stdout=PIPE, stderr=STDOUT)
output = p2.communicate()

print("output:")
print(output)
print()
