lst=[]
for i in range(1,200):
    if i%7==0:
        if i%5!=0:
            lst.append(i)
for l in lst:
    if l == lst[-1] :
        print(l)
    else:
        print(l,end=",")  #end=  >>> print 다음 enter를 end값으로 변환


lst = []
for i in range(1,200):
    if i%7==0 and i%5!=0:
        lst.append(i)

print(lst)
