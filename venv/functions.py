# Functions
#Function is a collection of statements to perform an operation
#To define a function we use "def" keyword
#The function which is defined once can call for multiple times
#To call a function we use function name:
#syntax def function-name():
#indentation

def display():
    print ("Hi")
    print ("Iam on display")
print ("one")
display()
print("Two")

print ("-------------")


def show():
    print ("Iam on display")
print("one")
show()
print ("two")
show()
print ("Three")
show()
print ("Bye")
print("-----------")

#Example script on multi functions


def fun1():
    print ("Hello")
def fun2():
    print ("Hie")
fun2()
fun1()
print ("-----------")

def fun3():
    print ("bye")
fun3()
fun2()
fun1()
print ("-----------")


#In function defination calling another function

print("Hi")
def display():
    print ("Hello")
def show():
    print("My Name")
    display()
show()
print ("Bye")
print ("-----------")


def func1():
    print ("Function1")
    func2()
def func2():
    print ("Function2")
def func3():
    func2()
    print ("Function3")
    func1()
    print ("--------")
func3()
func1()
print("---------")



#Local Variable after these