# ord('a') = 97,  ord('z') = 122 , ord('A') = 65, ord('Z') = 90
# ord('0') = 48 ord('9') = 57


Word = input()

Lupper = 0
Llower = 0

for i in Word:
    if  65 <= ord(i) <= 90:
        Lupper += 1
    elif 97 <= ord(i) <= 122:
        Llower += 1
        

print('UPPER CASE {}\nLOWER CASE {}'.format(Lupper,Llower))
