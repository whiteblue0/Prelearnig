a = {
    '아메리카노': 1900,
    '카페모카': 3300,
    '에스프레소': 1900,
    '카페라떼': 2500,
    '카푸치노': 2500,
    '바닐라라떼': 2900
}

b = {
    '헤이즐럿라떼': 2900,
    '카페모카': 3300,
    '밀크커피': 3300,
    '아메리카노': 1900,
    '샷크린티라떼': 3300
}
x = {**a, **b}

x = sorted(x.items(), key= lambda n: n[0])
set(x)
menu = []

for i in range(len(x)):
    if x[i][1] >= 3000 :
        menu.append(x[i])



print('\{ {0},{1},{2} \}}'.format(menu[2],menu[0],menu[1]))
