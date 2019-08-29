class Circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        area = 3.14*(self.r**2)
        return area

a = Circle(2)
print('원의 면적: {}'.format(a.area()))