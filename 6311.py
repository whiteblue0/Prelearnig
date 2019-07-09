Board = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
#
# print(len(Board))

n1 = Board.count('A')*4
n2 = Board.count('B')*3
n3 = Board.count('C')*2
n4 = Board.count('D')

Result = n1 + n2 + n3 + n4
print(Result)
# # print(m)
# def Check(a):
#     a = list(a)
#     n1 = a.count('A')
#     print(n1)
#     n2 = a.count('B')
#     print(n2)
#     n3 = a.count('C')
#     print(n3)
#     n4 = a.count('D')
#     print(n4)
#     result = n1*4 + n2*3 + n3*2 + n1
#     print(result)
#
# Check()