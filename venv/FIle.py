# Read name and no of times to print and display from user

name = input("Enter Name:")
no = int(input("enter the no of times :"))
print(name*no)


#write a program to read idno,name and salary from user and write into a file

import pickle as p

idno = int(input("enter idno :"))
name = input("enter name :")
sal  = float(input("Enter salary :"))

file = open("Demo.txt","wb")
p.dump(idno,file)
p.dump(name,file)
p.dump(sal,file)

file.close()



#example script to read binary data to file

import pickle as y
file = open("Demo.txt","rb")
idno = y.load(file)
print(idno)
name = y.load(file)
print(name)
sal = y.load(file)
print(sal)

#To read along id,name and salary

import pickle as z
file = open("Demo.txt","rb")
n = z.load(file)
m = z.load(file)
l = z.load(file)
file.close()
print("idno",n)
print("name",m)
print("sal",l)



#After this refer to operators