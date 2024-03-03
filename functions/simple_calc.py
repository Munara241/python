
# Task is to write a pyhton program which to perform simple arithmetic operations (+, -, *, /)
# It should take 2 numbers as user input. Also, take a arithmetic operation as user input.

def calc():
    num1 = float (input("enter first number: "))
    num2 = float (input("enter second number: "))

    oper = str(input (" Please enter operation: + - * / \n"))

    if oper ==  '+':
      return num1 + num2
    elif oper == '-':
      return num1 - num2
    elif oper == '*':
      return num1 * num2
    elif oper == '/':
      return num1 / num2
    else:
      return ("wrong symbol")

var1 = calc ()
print (var1)
