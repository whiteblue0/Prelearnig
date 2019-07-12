lst = input().split(', ')
lst = [int(num) for num in lst]
lst = [num for num in lst if num%2 !=0]

for i in range(len(lst)):
    if i == (len(lst)-1):
        print(lst[i])
    else:
        print(lst[i],end=', ')