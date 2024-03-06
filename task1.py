
while True:
    age = int(input("Enter age:  "))
    if age < 13:
        print("Sorry you don't allowed to pass")
    elif 13 < age < 18:
        print ("Call your legal guardian")
    elif age >= 18:
        print("welcome")