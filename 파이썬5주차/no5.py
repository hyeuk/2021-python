sports = ['축구','야구','농구','배구']
num = [11, 9, 5, 6]

print('메소드 insert()로 팀원 수 삽입')
sports.insert(1,11)
sports.insert(3,9)
sports.insert(5,5)
sports.insert(7,6)
print(sports)
sports.remove(11)
sports.remove(9)
sports.remove(5)
sports.remove(6)

space = "''"
print('메소드 insert()로 {} 삽입'.format(space))

sports.insert(1,'')
sports.insert(3,'')
sports.insert(5,'')
sports.insert(7,'')
print(sports)
sports.remove('')
sports.remove('')
sports.remove('')
sports.remove('')
print('슬라이스 sports[1::2]에 num을 대입')
sports.insert(1,num[0])
sports.insert(3,num[1])
sports.insert(5,num[2])
sports.insert(7,num[3])
print(sports)






