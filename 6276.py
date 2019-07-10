Base = list(range(1,10))

result = []
# solution 1
#
#
# def Goo(n):
#     k = []
#     for i in range(len(Base)):
#         cnt = Base[i]*n
#         if cnt%3 != 0 and cnt%7 != 0:
#             k.append(cnt)
#     result.append(k)
#
# for i in range(2,10):
#     Goo(i)
# print(result)
#


#   solution2
def Goo2(n):
    for i in range(2,n):
        k = [num*i for num in Base if (num*i)%3 !=0 and (num*i)%7 != 0]
        result.append(k)

Goo2(9)
print(result)

# [[2, 4, 8, 10, 16], [], [4, 8, 16, 20, 32], [5, 10, 20, 25, 40], [], [], [8, 16, 32, 40, 64]]
# [[2, 4, 8, 10, 16], [], [4, 8, 16, 20, 32], [5, 10, 20, 25, 40], [], [], [8, 16, 32, 40, 64], []]