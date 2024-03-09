#Task 8

tip = 0
while tip != 14.99 and tip !=19.99:
    tip = int(input("Please enter tip amount: "))

if tip == 14.99:
    print("Standard")

elif tip == 19.99:
    print("Good")

# Loop should continue until you enter 14.99 that should print Standard,
# and 19.99 that should print Good


# #Task 9

fruit = ["pineapple", "apple", "banana", "grapes"] #fruit list
fruit.append("tomato")
print(fruit)

# Print new fruits list including tomato


# #Task 10

dict1 = {"apple": 50, 5: 76, "grapes": "good"}
dict1["grapes"] = 75
print(dict1)
print(dict1[5])
dict1["Hello"] = "Goodbye"
print(dict1)
print(dict1["apple"] + dict1["grapes"])
# #replace grapes value to 75
# #get the value of key "5"
# #Add a key value "Hello" = "Goodbye"
# #Print the sum of values of "apple" and "grapes"