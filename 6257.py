fruit = ['   apple    ','banana','  melon']

fruit = [i.strip() for i in fruit ]

fruitdic={}
for i in range(len(fruit)):
    fruitdic[fruit[i]]=len(fruit[i])

print(fruitdic)