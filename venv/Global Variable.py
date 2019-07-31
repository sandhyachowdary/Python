#Global Variable
#The variable which is declared inside the python file and outside the function or class are called as global variable
#The Global variable will get memory while running the program
# The scope of global variable is any where .It means we can use through at the python file and another python fine aslo


#Example

a = 100 # Global Variable
def show():
    print("Hello")
    b= 200 # Local Variable
    print(a+b)
c = 300 #Global Variable
print(a+c)
show()
print(a+c)

print("-----------")

#Global and Local Variable
a = 300
def display():
    a= 200
    print(a)
print(a)
display()
print(a)

print("-----------")


#Declaring global variable inside a function
#To declare global variable inside a function we use "global" keyword

a = "sandhya" #Global Variable
def show():
    print(a)
    global b
    b = 300
    c = 400
    print(b) #Global Variable
    print(b+c) #Local Variable
print(a)
show()
print(a)
print(b)
print("---------")

#The global variable which is declared inside a function will get memory when function is called
#ex: modify global variable inside a function

a = 10
def display():
    global a
    a = 20
    print(a)
print(a)
display()
print(a)


#parameters file after these
