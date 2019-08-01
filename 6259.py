
# print(ord('a'),ord('z'),ord('A'),ord('Z'),ord('0'),ord('9'))
# ord('a') = 97,  ord('z') = 122 , ord('A') = 65, ord('Z') = 90
# ord('0') = 48 ord('9') = 57


Word = input()

Lnum = 0
Dnum = 0

for i in Word:
    if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
        Lnum += 1
    elif 48 <= ord(i) <= 57:
        Dnum += 1
        

print('LETTERS {}\nDIGITS {}'.format(Lnum,Dnum))

