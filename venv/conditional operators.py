#wap to read 2no from user and print bignoor same
no1 = int(input("1stno: "))
no2 = int(input("2ndno: "))

if no1 > no2:
    print (no1 ,"is big")
if no2 > no1:
    print (no2, "is big")
if no1 == no2:
    print ("Both are same")
print ("thanks")



#example of if else:

no1 = int(input("1stno:"))
no2 = int(input("2ndno:"))
if no1 > no2:
    print(no1,"is big")
else:
    if no2 > no1:
        print(no2,"is big")
    else:
        print("Both are same")
print("thanks")


#example on if elif else

no1 = int(input("1stNo"))
no2 = int(input("2ndNo"))

if no1 > no2:
    print(no1,"is big")
elif no2 > no1:
    print(no2,"is big")
else:
    print("Both are same")
print("Thanks")




#wap to validate username and password

uname =input("Enter Username")
pwd   = input("Enter password")

if(uname == "sandhya"):
    if(pwd == "password"):
        print("welcome user")
    else:
        print("enter valid password")
else:
    print("enter valid username")

#write a script to ATM  withdraw process

#check pinno
#withdraw * of 100
#max withdraw is 10000
#check balance

pinno = int(input("Enter pin no:"))
amount = int(input("Enter Amount"))
if pinno == 9876:
    if amount %100 == 0:
        if amount < 10000:
            print("Please collect your cash")
        else:
            print("Enter valid amount")
    else:
        print("please enter amount in multiplies of hundred only")
else:
    print("entered pin invalid")


# Given an int n return the absolute difference between n and 21 except retrun double the absolute diff if n is


def diff21(no):
    if no < 21:
        return 21-no
    else:
        return (no-21)*2
x = diff21(int(input("enter no :")))
print("diff is :",x)




#We have a loud talking parrot.The "hour" parameter is the current hour time in the range 0.23. we are in trouble if the
#parrot is talking and the hour is before 7 or after 20 .Return  True if we are in trouble



def parrot_trouble(talking,hour):
    if talking:
        if hour < 7 or hour > 20:
            return True
        else:
            return False

res = parrot_trouble(True,6)
print(res)
res = parrot_trouble(True,13)
print(res)



#a_smile and b_smile indicate  if each is smiling.we are in trouble if they are both smiling or if neither of them is smiling
#return true if we are in trouble
#monkey_trouble(True,True) -> True
#monkey_trouble(Flase,False) -> True
#monkey_trouble(True,False) -> False

def monkey_trouble(a_smile,b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False
print(monkey_trouble(True,False))
print(monkey_trouble(False,False))
print(monkey_trouble(True,True))



#------------for file after these --------