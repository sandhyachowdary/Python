num = float(input("Enter a number"))

if num>0:
    print("{0} is a positive number".format(num))

elif num == 0:
    print("{0} is zero".format(num))
else:
    print("{0}  is negative number".format(num))





num = int(input("Enter a number ="))
if (num % 2)==0:
    print("{0} is Even number ".format(num))
else:
    print("{0} is odd number".format(num))



year = int(input("Enter year ="))
if(year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))





num = int(input("Enter a number ="))
if num> 1:
    for i in range(num,2):
        if (num % i):
            print(num,"is not a prime number")
            print("times",num//i,"is",num)
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")



lower = int(input("Enter a lower number ="))
upper = int(input("Enter a upper number ="))

for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)







num = int(input("Enter a number"))
fac = 1
if num < 0:
    print("sorry fac 0 is not possible")
elif num == 0:
    print("Fac of 0 is 1")
else:
    for i in range(1,num+1):
        fac = fac * i
    print("The fac",num,"is",fac)





num = int(input("show mul table of ?"))

for i in range(1,11):
    print(num,'x',i,'=',num*i)









nterms = int(input("How Many terms you want ? "))

n1 = 0
n2 = 1
count = 2
