student1 = (90, 80)
student2 = (85, 75)
student3 = (90, 100)
lst = [ ]

def TupleCal(a):
    cnt = (a[0]+ a[1])
    Average = cnt/2
    return (cnt, Average)

c1 = TupleCal(student1)
print("1번 학생의 총점은 {}점이고, 평균은 {}입니다.".format(c1[0],c1[1]))

c2 = TupleCal(student2)
print("2번 학생의 총점은 {}점이고, 평균은 {}입니다.".format(c2[0],c2[1]))

c3= TupleCal(student3)
print("3번 학생의 총점은 {}점이고, 평균은 {}입니다.".format(c3[0],c3[1]))
