def Find(lst,n):
    for i in range(len(lst)):
        if n == lst[i]:
            print(f"{n} => True")
            return i

    return print(f"{n} => False")

lst1 = [2, 4, 6, 8, 10]

print(lst1)
a = Find(lst1,5)
b = Find(lst1,10)
