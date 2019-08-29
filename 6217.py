class Student:
    def __init__(self, name):
        self.name = name

class GraduateStudent(Student):
    def __init__(self, name, major):
        self.name = name
        self.major = major

m1 = Student('홍길동')
m2 = GraduateStudent('이순신','컴퓨터')

print('이름: {}'.format(m1.name))
print('이름: {}, 전공: {}'.format(m2.name, m2.major))