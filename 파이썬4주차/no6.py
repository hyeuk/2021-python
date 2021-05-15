from random import randint

while True:
    
    y = randint(1,99)
    n = randint(1,99)
    yn = input('계속y / n ?')
    if yn == 'n':
        print('프로그램을 종료')
        break
    
    else:
        print('{} * {} = {}'.format(y,n,y*n))
        
        
