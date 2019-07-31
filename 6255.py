import operator

data = {
    "TV": 2000000,

    "냉장고": 1500000,

    "책상": 350000,

    "노트북": 1200000,

    "가스레인지": 200000,

    "세탁기": 1000000,
}

sortdata = sorted(data.items(), key=operator.itemgetter(1),reverse=True)

for i in range(len(sortdata)):
    temp = sortdata[i]      
    print('{}: {}'.format(temp[0], temp[1]))