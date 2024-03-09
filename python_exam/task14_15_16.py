#Task 14

def add(i, j, k, l):
    return i + j + k + l
# User needs to input only 2 variables, and it should add 5 and 6 to the sum
# eg. user inputs 2 and 3, total should be: 2+3+5+6=16

val1 = float(input("Provide 1st value: "))
val2 = float(input("Provide 2nd value: "))

oper = input("""Choose option: 
+ add
Input: """)

if oper == "+":
    total = add(val1, val2, 5, 6)
    print(f"total value is: {total}")

#Task 15

And = [4,5,2,5,6]
print(And[-1])  # print last value (6) from the list

#Task 16

def days():
    day = years*365 
    return day

years=int(input("Enter number of years: "))
unit=int(input("""Pick your choice:  
1 - Days
2 - Weeks
Input: """))

if unit == 1:
    w=days()
    print(w)
