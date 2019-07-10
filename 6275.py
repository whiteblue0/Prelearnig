Sentence = list('Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.')

Sentence.count('a')
def Delstr(x):
    cnt = Sentence.count(x)
    i = 1
    for i in range(cnt):
        Sentence.remove(x)
        i+=1

Delstr('a')
Delstr('e')
Delstr('i')
Delstr('o')
Delstr(('u'))
TransSentence = ''.join(Sentence)
print(TransSentence)