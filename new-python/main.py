

# Data types
# Integer - whole numbers
# Float - decimal numbers
# String - sequence of characters
# boolean - True, False

calc_units = 24 * 60 *60
print (calc_units)

# 5 days are equal to XXXX seconds
# this is how we concatinate string with other data/variables

# print( f"10 days are equal to {10*calc_units} seconds")
# print( f"15 days are equal to {15*calc_units} seconds")
# print( f"20 days are equal to {20*calc_units} seconds")
# print( f"25 days are equal to {25*calc_units} seconds")

# functions - are used to make our code more dinamic.
# Essentialy, the function is a block of code, and it is used to avoid repetition.
# functions take arguments as parameters, in paranthesies. There can be 1, 2, 3 and more arguments passed to a function.

def days_to_unit(num_days):
    # some code
    print( f"25 days are equal to {num_days*calc_units} seconds")

# In order to use the function, you have to call in your code by using the name of the function (without def)
    

days_to_unit(10)  
days_to_unit(15)
days_to_unit(20)
days_to_unit(25)