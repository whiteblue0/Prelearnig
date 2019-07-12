import math

a = input().split(', ')

a = list(a)
a = [round(2*math.pi*float(num), 2) for num in a]

for i in range(len(a)):
    if i == (len(a)-1):
        print(a[i])
    else:
        print(a[i], end=', ')