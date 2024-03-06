# 1.calculate the sum

# sum = 0
# for i in range(1,101):
#     sum += i
# print (sum)

# 2.count from 100 to 1

# for i in range(100,0,-1):
#     print(i)

# 3.Even numbers
# val = [0,1,2,3,4,5,6,7,8,9,10]
# for i in val:
#     if i % 2 == 0 and i != 0:
#         print (i)

# 4.multiply by enter number
# num = int(input("Enter number"))
# for i in val:
#    num2 = num * i
#   print(num2)
# num = int(input())
# for i in val:
#     print(f"{num}*{i} is {num*i}")

# 5.for each 3rd number add foo
# for each 5th number add bar
# for each 10rd number add buzz

for i in range(100):
    output = str(i)
    if i % 3 == 0:
        output = output + "foo"
    if i % 5 == 0:
        output = output + "bar"
    if i % 10 == 0:
        output = output + "buzz"
    print(output)