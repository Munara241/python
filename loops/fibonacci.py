# Fibonacci sequence

limit = int(input("Enter a limit:  "))
num1 = 0
num2 = 1

next = num1 + num2   # num1 = 0, num2 = 1, next = 1 .. num1 = , num2 = , next = 
print (num1)
print (num2)

while next < limit:
    print(next)

    num1 = num2
    num2 = next
    next = num1 + num2