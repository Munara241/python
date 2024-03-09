#Task 5

def add_numbers(a, b):
    result = a + b
    return result

sum = add_numbers(5, 10)
print(f"The sum is: {sum}")


# Task 6
x = 10
y = "20"  # don't touch this line
print(x + int(y))  # should print 30


# Task 7
val = (0,1,2,3,4,5,6,7,8,9,10)
#Print only numbers: 3, 6, 9
for hello in val:
    if hello % 3 == 1 and hello != 0:
        print(hello)