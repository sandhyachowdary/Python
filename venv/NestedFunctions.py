#Nested Functions:
#               A function defined in another function is called nested function
#               The scope of nested function is with in the other function
#               outer function local variable can access by inner function

#ex
def outer():
    print("Iam outer")
    def inner():
        print("I am inner")
    inner()
outer()

#using local variable of outer function in inner function

def outer():
    print("Iam outer function")
    a = 100
    def inner():
        print("Iam inner")
        print(a)
    inner()
    print(a)
outer()

#Modify Local variable of outer function in inner function

def outer():
    a = 100 #local variable
    print(a)
    def inner():
        a = "sandhya" #Local of inner
        print(a)
    inner()
    print(a)
outer()

#In above example inner function is not modifying outer function variable,to do so we need to declare varaible with
# "Non Local"  keyword
def outer():
    a =100
    print(a)
    def inner():
        nonlocal a
        a = "Sandhya"
        print(a)
    inner()
    print(a)
outer()

#Outer function with required parameter
def outer(name):
    def inner():
        nonlocal  name
        name = "Mr/Mrs :" + name
    inner()
    print(name)
outer(input("Enter name :"))

#In the above example what should happen if the last value of the function() returned the inner()  function instead of calling it?
# Closer:
#points to create closer:
#-> We must have a nested function(function inside a function)
# -> The nested function must refer to value defined in outer function
# -> The outer function must return inner function
#ex:
def outer(name):
    def inner():
        nonlocal  name
        name = "Mr/Mrs :" + name
        print(name)
    return inner
inn = outer("Sandhya")
del outer
inn()

#Passing function name as argument

def inc(no):
    no+= 1
    return no
def dec(no):
    no-= 1
    return no
def count(fun,no):
    res = fun(no)
    print(res)
count(inc,100)
count(dec,20)


#---------After this Error Handling File ---------