#The function which is calling it itself  is called "Recursive" function
count = 1
def show():
    global count
    print("Iam show :", count)
    count = count+1
    show()
show()


# after this refer to sample program

