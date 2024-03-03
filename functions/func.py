# convertation days to minutes.

calc_min = 24 * 30

num1 = calc_min * 100

def days (n,m):
    print (f"{n} day are {n * calc_min} minutes")
    print(m)

def days_sec (x, m):
    print (f"{x} day are {x * calc_min} seconds")
    print(m)

days (40, "whatever")
days_sec (10, "whatever")

