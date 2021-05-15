h = 'HelloPython!'
hello = list(h)


a = '+ 012345678901'
b = '- 210987654321'
print(a)
print('{:^17s}'.format(h))
print(b)

while True:
    
    a,b,c = input('슬라이스[?:?:?] 3개 입력 >>').split()
    d,e,f = int(a),int(b),int(c)
    if d < 1:
        print('종료'.center(20,'*'))
        break
    elif e < 1:
        print('종료'.center(20,'*'))
        break
    elif f < 1:
        print('종료'.center(20,'*'))
        break
    
    
    else:
        print(hello[d:e:f])
