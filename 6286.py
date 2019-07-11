def Pibo(k):
    n1 = 0
    n2 = 1
    lst = [n2]
    for i in range(k-1):
        n3 = n1+n2
        n1 = n2
        n2 = n3
        lst.append(n2)
        i+=1

    print(lst)

Pibo(10)