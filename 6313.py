def TransASCII(x):
    n = chr(x)
    print("ASCII 65 => %s" % n)
    return n

# ord('str') => 문자를 ASCII코드값으로 변환
# chr('int') => ASCII코드값을 문자로 변환

TransASCII(65)