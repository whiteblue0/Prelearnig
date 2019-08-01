class Student:
    def __init__(self,x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self):
        add = self.x + self.y + self.z
        print('국어, 영어, 수학의 총점: {}'.format(add))

lst = list(map(int, (input().split(', '))))
a = lst[0]
b = lst[1]
c = lst[2]

a = Student(a,b,c)
a.add()