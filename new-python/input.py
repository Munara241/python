
# user input is a function that allow for a user to enter(input) some information
# when user input is taken by a function, it is stored inside a variable
# function saves the input in string format, and if you another data type, u have to use casting.

first = input("What is your name?")
last = input("What is your last name?\n ")
print(f"Hello,{first} {last}")

var = input("Enter a number: ")
print (type(var))

# In order to convert str to integer we use casters
num = int(var)
print(type(num))

num1 = int(input())
print(num1)
print(type(num1))