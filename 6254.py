PhoneBook = {
    '홍길동': '010-1111-1111',
    '이순신': '010-1111-2222',
    '강감찬': '010-1111-3333'
}


print('아래 학생들의 전화번호를 조회할 수 있습니다.')
for key in PhoneBook.keys():
    print(key)

name = input()
if name in PhoneBook.keys():
    print('이순신의 전화번호는 {}입니다.'.format(PhoneBook[key]))