# Raise:
#   Raise is a keyword used to return exception to called place

def checkage(age):
    if age >= 23:
        return "Valid Age"
    else:
        raise ValueError("Invalid Age")
a = int(input("Enter Age:"))
try:
    x = checkage(a)
    print(x)
except ValueError as T:
    print(T)
print("thank")



#Assert:
#       Assert is a keyword used to check a condition and will return Assertion Error

def CheckAge(Age):
    assert age >= 23, "Invalid Age"
    return "Validage"
age = int(input("Enter Age:"))
try:
    x = CheckAge(a)
    print(x)
except AssertionError as ae:
    print(ae)
print("thanks")