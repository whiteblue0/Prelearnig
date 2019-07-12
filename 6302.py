lst = [12, 24, 35, 70, 88, 120, 155]

lst = [i for i in lst if i != lst[0] and i != lst[4] and i != lst[5]]

print(lst)