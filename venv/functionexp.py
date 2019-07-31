# What is function?
#Function is a collection of statements to perform oprations

#Advantages of function
# -> code Reusablity easy to modify easy to debug

#How functions make development further
#-> Ignoring the relation of code

# How to define and call function
# To use def keyword and call the function we should use function-name

#what the difference between define and calling a function
#In function defination we declare the statements by calling the function we are performing the operation

# can we call a function inside of another function
#yes


#How many times we can call a function
# Multiple times

#What is local variable
#A Variable declare inside a function

#what is the scope of local variable
#From function declaration to function ending


#can we declare local variables with same name in different function
#yes


#In python we can define functions in 4 ways:
#function without arguments and without return
#function with arguments and without return
#function without arguments and with return
#function with argument and with return


#arguments can be n no
#return will be only one[1]



#Example on function without arguments without return:

def add():
    a=10
    b=40
    print(a+b)
add()



#Example on function with arguments and without return:
def add(no1=0, no2=0):
    print("sum of =", no1+no2)

add()
add(20)
add(20,30)
add(no2=40)
add(no2=30,no1=20)
add(no2=5,no1=-20)

print("-----------")


#Return: Return is a keyword, which is used to return one object at a time
#Return  must be last statement in a function because once controller execute return statement LTE function will get terminated

#syntax: def function-name():
#       ----------
#       ----------
#       return object
#       -----------
# function calling()

#example on function without argument and with retrun:

def add():
    a = 10
    b = 30
    return a+b
x =add()
print("sum =",x)

print("----------")

#example on function with argument with return type

def add(no1,no2):
    return no1+no2
x =add(10,20)
print("sum =",x)
#(or)
print("sum =", add(10,15))

print("--------")

#we can find length of string,list,set,tuple

s1 ="satya"
a = len(s1)
print("length =", a)
print("length =",len(s1))


#After this recursive function