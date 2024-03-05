
# calculation of cloud services prices
# Ask user to enter an hourly cost of running one server
# Ask the user to choose btw calculating the monthly cost or the yearly cost
# Calculate and bring the estimated cost based on the user's selection

hourly_cost = int(input("Please enter hourly cost of running a server: "))
choice = str(input(""" Please choose monthly or yearly cost:
                monthly
                yearly
                \n"""))
if choice == "monthly":
    mon_cost = hourly_cost * 24 * 30
    print(f" Monthly cost will be ${mon_cost}")

if choice == "yearly":
    year_cost = hourly_cost * 24 * 30
    print(f" Yearly cost will be ${year_cost}")
else:
    print("Wrong choice")