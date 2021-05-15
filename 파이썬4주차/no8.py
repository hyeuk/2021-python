from random import randint
operator = ['+','-','*','/','%']
f = randint(1,100)
print('첫 값은 {}이다.'.format(f))

while True:
    
    c = input('산술 연산의 종류를 입력하세요. >>')
    if c not in operator:
        print('종료'.center(30,'*'))
        break
    s = int(input('두 번째 피연산자를 입력하세요. >>'))
    
    result1 = f + s
    result2 = f - s
    result3 = f * s
    result4 = f / s
    result5 = f % s
    
    if c in '+':
        print('{} {} {} = {}'.format(f,c,s,result1))
    elif c in '-':
        print('{} {} {} = {}'.format(f,c,s,result2))
    elif c in '*':
        print('{} {} {} = {}'.format(f,c,s,result3))
    elif c in '/':
        print('{} {} {} = {}'.format(f,c,s,result4))
    elif c in '%':
        print('{} {} {} = {}'.format(f,c,s,result5))
    
    
