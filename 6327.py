def Square(n):
    k = n**2
    print(f"square({n}) => {k}")

a, b = map(int, input().split(','))
Square(a)
Square(b)