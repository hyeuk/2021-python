korean = ('정렬','초보자','내포','사전')
english = ('sorting','novice','comprehension','dictionary')



while True:
    word = input('찾을 단어 입력 ? ')
    
    if word == '정렬':
        print(english[0])
    elif word == '초보자':
        print(english[1])
    elif word == '내포':
        print(english[2])
    elif word == '사전':
        print(english[3])
    else:
        print('찾으시는 단어가 없습니다.')
        break
    


