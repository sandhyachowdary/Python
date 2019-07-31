#parameters or Arguments:
#The variable which is declared  in function Header and with in the parathesis '()' is called parameters
#The parameter will get memory when function is called
#The scope of parameter is throughout the function
#In python the parameters (or) arguments are 4types:
#1.Required arguments
#2.Default arguments
#3. Arguments Length
#4. keyword Arguments



# Eg: Example on "Required arguments"
#In a function is defined with "Required Arguments",while calling the function we must and should pass values else it will return error

def display(a,b):
    print (a+b)
display(10,20)
display(10.5,20.5)
display("sandhya","chowdary")
display(True,False) # True= 1 ,False =0 a=1,b=0 => 1+0=1
display([10,20,30],[40,50]) # List will not perform addition operation they will just combine the values and display
display((10,"sandhya",False),(40,50)) # set will not perform addition operation they will just combine the values and display


#Eg: "Default Arguments"
def display(a=0,b=2):
    print (a+b)
display()
display(90)
display(10,20)


#If a function is defined with default arguments no need to pass  values while passing function


def show(idno=0, name = None, salary =0.0):
    print("employeeidno =",idno)
    print("employee name =", name)
    print("employee salary=", salary)
show()
show(101)
show(101,"sandhya")
show(101,"sandhya",1850000.00)
show("rani")
#keyword arguments (or) named arguments

show(name="sandhya",idno=191)


def display(idno, name=None, salary=0.0):
    print("employee idno = ", idno)
    print("employee Name = ", name)
    print("employee salary =", salary)


display(101)
display(101,'Ravi')
display(name = "sandhya", idno= 101)





# If a function is defined with required and default arguments  required argument must be displayed first else it returns syntax error




#functions exp after these