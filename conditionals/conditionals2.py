# conditions with elif

u = int(input())
if u < 13:
    print('child')
elif u >= 13 and u < 18:
    print('teenager')
elif u >= 18 and u < 65:
    print('adult')
else:
    print('elder')