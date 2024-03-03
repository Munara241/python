
# Task. Create a python program that is supposed to take a product price as user input.
# It should have 2 functions, to calculate tax and
# to calculate discount (10% if price is >80).
# IT should print total price at the end.

def cal_tax(price):
    tax = price * 0.08
    return tax

def calc_dis(price, dis_per):
    dis = price * (dis_per/100)
    return dis
    
prod_price = float (input("Enter the price of product: "))
tax = cal_tax(prod_price)

if prod_price > 80:
    dis = calc_dis(prod_price,10)
    
total_price = prod_price + tax - dis
print (total_price)
