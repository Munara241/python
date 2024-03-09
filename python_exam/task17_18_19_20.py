#Task 17

def add(a, b):
    if a == b:
          return a + b   # Modify inside of the function to print 10 and 25
    else: 
         return a + b + 4
# Don't touch lines below
w = add(5,5)
print(w)         # should print 10

x = add(10,11)
print(x)        # should print 25

#Task 18

sum = 0
list = ()

while sum < 100:
    number = int(input("Enter the number:"))
    sum += number
    list.append(number)
print(list)   # should accept numbers until sum reaches 100 and prints all numbers

#Task 19

def calculate_tax(price):
	tax = price * 0.08
	return tax

def Sum(price, tax, discount):
	price = price + tax - discount 
	return price

price = float(input("Please enter the price: "))  
tax = calculate_tax(price)
print(Sum(price, tax, 10, ))

#Task 20

# Print numbers up to 100 and for every third add foo,
# every 5th add bar, every 10th add buzz
for i in range(100):
    output = str(i)
    if i % 3 == 0:
        output += " foo"
    if i % 5 == 0:
        output += " bar"
    if i % 10 == 0:
        output += " buzz"
    print(output)