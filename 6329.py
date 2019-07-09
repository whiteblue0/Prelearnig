def countdown(n):
    int(n)
    if n < 1:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    else:
        while n:
            print(n)
            n -= 1

countdown(0)
countdown(10)