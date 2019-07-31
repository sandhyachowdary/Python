#Local Variable
# Variable which is declared inside the function body is called as local variable
# The Local variable will get memory when the function is called
# The scope of local variable is from declaration to function ending


#Example


def show():
    print("hello")
    a = 100 # local variable
    print(a)
show()
print ("---------")



def display():
    print("Hello")
    a=100
    b=200
    print(a+b)
    print("Bye")
display()


#Global variable after these