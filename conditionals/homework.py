
# Task 2: A food delivery asked you to print out a message depending on the tip % percentage a customer has left,
#  print out standard ( 15% ), good ( 18%), great ( 20%) , my hero ( >20% ),
# depending on the input placed by customer.

tip = int(input(f"Enter your tip: "))
if 18 > tip >= 15:
    print("standart") 
elif 20 > tip >= 18:
    print("good")
elif tip == 20:
    print("great")
else:
    print("My hero!")