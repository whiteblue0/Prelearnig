n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

num = [n1, n2, n3, n4, n5]
Avg = [sum(num)/len(num)]
avg = Avg.pop()
print("입력된 값 {}의 평균은 {}입니다.".format(num,avg))