#To read input from keyboard we use "input()" function
# Then input() function will return any given input in string format only

#ex:
name = input("enter name: ")
print("welcome:", name)
# example script to read two numbers from user and print sum

no1 = input("1st No:")
no2 = input("2nd No:")
print("Sum = ", no1+no2)
#In the above example the input function is returning string and we are concatinating two strings

#int():
# This function will take string as a argument and convert it into "int" and return int value
#int("100")-> correct
#int("abc") -> wrong
#int("10.25) -> wrong


#ex
s1 = input("1stno: ")
s2 = input("2ndno: ")

no1 = int(s1)
no2 = int(s2)

print("sum = ", no1+no2)

#       or

a = int(input("1stno: "))
b = int(input("2ndno: "))
print("sum =", a+b)


#       or


print("Sum =", int(input("1stno:")) + int(input("2ndno: ")))





#FLoat(): This function will take string as argument and convert it into "float" and return float value
#float("10.25") correct
#float("abc") wrong
#float("100") correct



#
print("sum =", float(input("n01: "))+float(input("no2: ")))




#example on evaluate function

x = eval(input("Enter a value:"))
print(x)
print(type(x))

#out put
# enter a value = 11.4 ,11
# 11.4,11
#<class 'float> <class 'int'>
# enter value = "sandhya"
#sandhya
#<class 'str'>
#enter a value = [10,20,30]
#[10,20,30]
#<class 'list'>
#enter a value = {10,20,30}
#{10,20,30}
#<class 'set'>
#enter a value = True
#True
#<class 'bool'>
#enter a value = (10,20,30)
#(10,20,30)
#<class 'tuple'>
# enter a value = {1:'A', 2:'B'}
#{1:'A', 2:'B'}
#<class 'dict'>



# After this refer to filesandhy







