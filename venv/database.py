#Example program to insert data in to table
import sqlite3 as sql
conn = sql.connect("icici.db")
curs = conn.cursor()
try:
    curs.execute("insert into savingsaccounts values(1001,'sandy',9876543210,350000,'active')")
    conn.commit()
    print("Data inserted")
except sql.integrityerror:
    print("Account no is available")
conn.close()
print("connection closed")

#Example program to create a table

import sqlite3 as sql
conn = sql.connect("icici.sqlite3")
curs = conn.cursor()
try:
    curs.execute("create table savingsaccounts(acno number primarykey,name text,contact number unique,balance real,status text)")
    print("Table created")
except sql.operationalerror:
    print("Table available")
conn.close()
print("connection closed ")
#example script to read from keyboard
a_no = int(input("enter account no:"))
a_name = input("enter name:")
a_cno = int(input("enter contact no:"))
a_bal = int(input("enter opening balance:"))
a_status = input("Account Status:")


#example script to read from keyboard

import sqlite3 as sql
conn = sql.connect("icici.db")
curs = conn.cursor()
curs.execute("insert into savingsaccounts values(?,?,?,?,?)",(a_no,a_name,a_cno,a_bal,a_status))
conn.commit()
print("Table Created")
conn.close()


#example script to read all account details from db


import _sqlite3 as sql
conn = sql.connect("icici.db")
curs = conn.cursor()
curs.execute("select * from savingsaccounts")
res = curs.fetchall() #will return the list of tuples
print(res)
conn.close()

#each tuple is one record (A row in a database)


#example script to read one[1] account details from db

a_no = int(input("enter account no: "))

import sqlite3 as sql
conn = sql.connect("icici.db")
curs = conn.cursor()
curs.execute("select * from savingsaccounts where a_no = ? ",(a_no,))
res = curs.fetchall()
print(res)
conn.close()


#example to read all contact numbers

import sqlite3 as sql
conn = sql.connect("icici.db")
curs = conn.cursor()
curs.execute("select contact no from savingsaccounts")
res = curs.fetchall()
print(res)
conn.close()
