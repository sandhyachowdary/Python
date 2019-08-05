#Define 4 functions add,sub,mul,div every function must be  with 2 arguments and with return one function need to call other function
#requried output must be +,-,*,/
#12
def add(a,b):
    return a+b
def sub(a,b):
    s = add(a,b)
    print("sum =", s)
    return a-b
def mul(a,b):
    s = sub(a,b)
    print("sub= ",s)
    return a*b
def div(a,b):
    m = mul(a,b)
    print("Mul =", m)
    return a/b
d = div(10,20)
print("div =",d)
print("thanks")




#after this refer to reading input from keyboard



#10
print("welcome sandhya")


#11
name = input("enter name :")
print("welcome",name)



#13
# type of variable

x = eval(input("Enter a value:"))
print(x)
print(type(x))


#14
x = input("Enter first name:")
y = input("Enter last name :")

w = str(x)
z = str(y)
print(x+y)



#18

stu = input("Enter students name")
marks1 = input("Enter marks1 =")
marks2 = input("Enter 2marks =")
marks3 = input("Enter 3marks =")

z = int(marks1)
w = int(marks2)
q = int(marks3)
print("total of marks =",z+w+q)
print("average of marks=", (z/w/q)/3)


#20

emp = input("employee id_no =")
name = input("employee name =")
salary = input("basic salary =")
HPA = input("HPA= ")
DA = input("DA=")

S = int(salary)
H = int(HPA)
D = int(DA)

print("Gross Salary =",S+H+D)

#19
x = 10
y = 5
x = x*y
y = x//y
x = x//y
print("After swaping: x =",x,"y =",y)


#(or)
num1 = input('Enter First Number: ')
num2 = input('Enter Second Number: ')

print("Value of num1 before swapping: ", num1)
print("Value of num2 before swapping: ", num2)

# swapping two numbers using temporary variable
temp = num1
num1 = num2
num2 = temp

print("Value of num1 after swapping: ", num1)
print("Value of num2 after swapping: ", num2)


#1
#what is python?
#Python is an interpreted, object-oriented, high-level programming language with dynamic semantics


#2
#what is programming language
#A programming language is a vocabulary and set of grammatical rules for instructing a computer or computing device to perform specific tasks.
# The term programming language usually refers to high-level languages, such as python.


#3
#what is software and how many types
#Computer software, or simply software, is a kind of programs that enable a user to perform some specific task or used to operate a computer.
#Types of software:
#1.user
#2.appplication software
#3.operating system
#4.Hardware

#4
# what is python script
#Basically, a script is a text file containing the statements that comprise a Python program.
# Once you have created the script, you can execute it over and over without having to retype it each time


#5
#What kind of applications we can develop using python
#Python is best suited for work related to maths & data.
# Python is a high-level general-purpose programming language that can be applied to many different classes of problems.

#6
#How to develop standalone application in python
#The easiest way to create an application from a Python script is simply by dropping it on the BuildApplication applet
# in the main Python folder. BuildApplication has a similar interface as BuildApplet: you drop a script on it and it will process it,
# along with an optional .rsrc file.


#7
#How to develop distributed application in python
#is a high-performance asynchronous messaging library aimed at use in scalable distributed or concurrent applications.
# It provides a message queue, but unlike message-oriented middleware, a ØMQ system can run without a dedicated message broker.
# The library is designed to have a familiar socket-style API.


#8
#Is python a case senstive language
#Yes, python  is a case senstive language


#9
#Where we can use python
#Python is a general purpose and high level programming language.
# You can use Python for developing desktop GUI applications, websites and web applications.

