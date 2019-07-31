#Define 4 functions add,sub,mul,div every function must be  with 2 arguments and with return one function need to call other function
#requried output must be +,-,*,/



def add(a,b):
    return a+b
def sub(a,b):
    s = add(a,b)
    print("sum =", s)
    return a-b
def mul(a,b):
    s = sub(a,b)
    print("Sub =", s)
    return a*b
def div(a,b):
    s = mul(a,b)
    print("mul = ",s)
    return a/b

d = div(10,2)
print("div =", d)
print("Thanks")


#after this refer to reading input from keyboard