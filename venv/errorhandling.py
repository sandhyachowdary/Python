#Example without exception Handling
a = int(input("1stno: "))
b= int(input("2nd no: "))
print("Sum =", a+b)
print("div =", a/b)
print("mul =", a*b)
print("sub = ",a-b)
print("thanks")

#output:
#1st no : 10
#2nd no :0
#sum = 10
#Zero division error: division by zero
#Exception is occured program is terminated Abnormally


#Example with exception Handling


a = int(input("1StNo: "))
b = int(input("2ndNo:"))
print("sum =", a+b)

try:
    print("div =",a/b)
except ZeroDivisionError as z:
    print(z)
print("mul =",a*b)
print("sub =",a-b)
print("Thanks")

#output
#1stno: 10
#2ndno: 0
#sum = 10
#Zero Division Error
#mul = 0
#sub = 10
#Thanks
#exception is occured and handled so normal termination

#Output
#1stno: 10
#2ndno: invalid literal for int with base 10
#Exeception will occured and program terminated abnormally if second value is not provided in the input
#Note:  To handle user -3 exception we need to define multiple except block




#Example of multi except blocks

try:
    a = int(input("1stNo:"))
    b = int(input("2nd No:"))
    print("Sum = ", a+b)
    print("Div = ",a/b)
    print("Mul = ",a*b)
    print("Sub =", a-b)
except ZeroDivisionError as zde:
    print(zde)
except ValueError:
    print("Invalid input")
print("Thanks")


#output:
#1st No: 10
#2nd No: 0
#sum = 10
#division by zero ( exception is handled normal termination but not complete output)
#Thanks

#output:
#1st No: Ten (invalid input)
#Invalid Input
#Thanks
#exception is handled and normal termination

#Note: In try blcok is any exception is occured the next statements in try blocks will be skipped like above 2outputs




#Example on nested try:

try:
    a = int(input("1stNo: "))
    b = int(input("2ndNo: "))
    print("Sum = ", a+b)

    try:
        print("Div =", a/b)
    except ZeroDivisionError as Z:
        print(Z)
    print("mul =", a*b)
    print("sub = ", a-b)
except ValueError:
    print("Invalid Input")
print("Thanks")


#output:                        #output:
#1stno : 10                     1stno: Ten
#2ndno : 0                      Invalid input
#sum = 10                       Thanks
#division by zero
#mul = 0
#sub = 10
#thanks

#example on Try  with else:


fname = input("enter filename or filepath :")
try:
    file = open(fname)
    data = file.read()
except FileNotFoundError as F:
    print(F)
else:
    print(data)
    file.close()
print("Thanks")

#example on try with finally:

lname = input("enter filename or path :")
try:
    file = open(lname)
    data = file.read()
except FileNotFoundError as T:
    print(T)
else:
    print(data)
finally:
    file.close()
print("Thanks")


#example on try and finally:
import sqlite3 as sql
conn = sql.connect("sample.db")
curs = conn.cursor()

try:
    curs.execute("insert into employee values(101,'sandhya',18000)")
    conn.commit()
finally:
    conn.close()
    print("DB connection closed")
print("Thanks")
