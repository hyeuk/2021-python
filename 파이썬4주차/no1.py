weather = int(input('월 입력'))


if weather < 4:
    print('{}월 겨울'.format(weather))
elif weather < 6:
    print('{}월 봄'.format(weather))
elif weather < 9:
    print('{}월 여름'.format(weather))
elif weather < 11:
    print('{}월 가을'.format(weather))
else:
    print('{}월 겨울'.format(weather))
