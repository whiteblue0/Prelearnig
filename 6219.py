n = int(input())
lst = []
for i in range(1, n+1):
    if n%i == 0:
        print("{}(은)는 {}의 약수입니다.".format(i,n))
        lst.append(i)
if len(lst) == 2:
       print("{}(은)는 1과 {}로만 나눌 수 있는 소수입니다.".format(n,n))