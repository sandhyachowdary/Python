



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