#Task 11

count = 10
while count > 1: # print count every iteration from 9 to 1
     count -= 1 
     print(count)


#Task 12

def days_weeks ():
    days = years * 365
    weeks = years * 52
    return days, weeks 

def months_hours ():
    months = years * 12
    hours = years *  365 * 24
    return months, hours

years = int(input("Enter number of years"))
days_weeks = days_weeks()
months_hours = months_hours()
print(days_weeks)
print(months_hours)

# It should print days and weeks for the 1st function, eg (365, 52)
# It should print months and hours for the 2nd function, eg (12, 8760)

#Task 13

x = 5
if x == 5:
    print("x is 5")
else:
    print("x is not 5")
