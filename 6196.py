
#a, i = map(int, input().split())
# a , n = 9, 4
a = int(input())
n = 4
a2 = a
Sum = a
for i in range(1,n):
    comp = a*10**i
    a2 = comp + a2
#   a2 += comp
    Sum+=a2
print(Sum)