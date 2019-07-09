a = input()

if a.isupper() or a.islower():
    b = a.swapcase()
    print("{}(ASCII: {}) => {}(ASCII: {})".format(a,ord(a),b,ord(b)))

else:
    print(a)
