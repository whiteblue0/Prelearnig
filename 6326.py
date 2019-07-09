def Facto(n):
    int(n)
    k = n
    for i in range(1,n):
        k *= n-i

    print(k)

n =int(input())
Facto(n)