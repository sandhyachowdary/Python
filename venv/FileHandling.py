#File Handling:
#File Opening:
#       To open a file we use open() function. It requires two arguments first the file path or file name,second which
#           mode it should open modes are like:
#   'r' - > open read only, you can read the file but can not edit / delete anything inside
#   'w' -> Open with write power means if LTE file exists then delete all content and open it to write
#   'a' -> Open in append mode

# Methods                                       Description
# read([number])                                return specified number if characters from the file ,if omitted it will
#                                               read the entire content of the file
# readline()                                    return the next line of the file
#readlines()                                    read all the lines as a list of strings in the file

#Note: The default mode is read only i.e if you donot provide any mode it will open the file as read only
#IN addition you can specify if the file should be handled as binary or text mode
#  "t" -> Text -> default value. Textmode
#  "b" -> binary -> binary mode


#example program to read data from a file

f = open("one.txt")
data = f.read()
f.close()
print("No of char's in file =", len(data))
lines = data.split("\n")
print("No of lines in file =", len(lines))
words = 0
for x in lines:
    words += len(x.split(" "))
print("No of words in file =",words)



#To open a file and read
print(open("one.txt").read())

# To read characters in file
f = open("one.txt")
data = f.read(3)
print(data)
f.close()


# To read line in file
f = open("one.txt")
data = f.readline()
print(data)
f.close()


# To read all lines in file
f = open("one.txt")
data = f.readlines()
print(data)
f.close()

# To read specific  line txt file
f = open("one.txt")
data = f.readlines()
print(data[0])
f.close()



f = open("one.txt")
data = f.read()
print("sandhya" in data)
print("python" in data)

#example program to write data in to file

f = open("sample.txt","w")
text = input("enteer text :") #to read data from keyword
f.write(text)
f.close()
print("Text written to file")


#example program on append mode
f = open("sample.txt","a")
text = input("enter text :")
f.write(text)
f.close()
print("text written to file")

#writing multiple line in file
f  = open("sample.txt","a")
text =  '''I am python student '''
f.write(text)
f.close()


#writing objects in to a file
import  pickle as pi
rno = 100
name = "sandhya"
marks = [10,20,30,40,50,60]
total = sum(marks)
file = open("employee.txt","wb") # write with binary
pi.dump(rno,file)
pi.dump(name,file)
pi.dump(marks,file)
pi.dump(total,file)
file.close()
print("data written in file")



#Reading objects from file

import  pickle as pi
file = open("employee.txt","rb")
rno = pi.load(file)
print(rno)
name = pi.load(file)
print(name)
marks = pi.load(file)
print(marks)
total = pi.load(file)
print(total)
file.close()


# After these with statements file refer