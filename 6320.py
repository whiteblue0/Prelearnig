lst = ["가위", "바위", "보"]

Man1 = input()
Man2 = input()
Hand1 = input()
Hand2 = input()

Man1 = Hand1
Man2 = Hand2


if Man1 == Man2 :
    print("Draw")
else:
    if Man1 == "가위":
        if Man2 == "바위":
            print("바위가 이겼습니다!")
            # print("Result : Man2 Win!")
        elif Man2 == "보":
            print("가위가 이겼습니다!")
            # print("Result : Man1 Win!")
    elif Man1 == "바위":
        if Man2 == "보":
            print("보가 이겼습니다!")
            # print("Result : Man2 Win!")
        elif Man2 =="가위":
            print("바위가 이겼습니다!")
            # print("Result : Man1 Win!")
    elif Man1 == "보":
        if Man2=="가위":
            print("가위가 이겼습니다!")
            # print("Result : Man2 Win!")
        elif Man2=="바위":
            print("보가 이겼습니다!")
            # print("Result : Man1 Win!")