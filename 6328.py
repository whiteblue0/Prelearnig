a ,b = input().split(', ')
def Long(i,j):
    l1 = len(i)
    l2 = len(j)
    if l1 > l2:
        print(i)
    elif l2 > l1:
        print(j)
    else:
        print("두 문자열의 길이가 같다.")

Long(a,b)