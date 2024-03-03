
# Create a python programm which takes user input, and then converts a number
# to days, weeks, month. Both the number and the proposed conversion unit


var = int(input("Enter the number of years"))
var2 = int(input("""Please choose which unit you want to convert to
             1 -days
             2 - weeks
             3 - month\n"""))
if var2 == 1:
    print(f"{var * 365} years")
elif var2 == 2:
    print(f"{var * 52} weeeks")
elif var2 == 3:
    print(f"{var * 12} month")
else:
    print("Wrong input")