a = int(input('소수인지를 판별할 2 이상의 정수 입력 >>'))
b = 0


for i in range(1,a+1):
    if a % i == 0:
        b=b+1

if b == 2:
    print('정수 {}은 소수이다.'.format(a))
else:
    print('정수 {}은 소수가 아니다.'.format(a))
    

