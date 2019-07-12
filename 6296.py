Words = input().split(', ')

Words.sort()

for i in range(len(Words)):
    if i == (len(Words)-1):
        print(Words[i])
    else:
        print(Words[i],end=', ')