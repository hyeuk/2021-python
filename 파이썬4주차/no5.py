c = 20 
 
for i in range(1,24,3):
    f = (c * 9/5) +32 
    sf = (c*2)+30
    print('섭씨: {} 화씨: {:.1f} 화씨(약식): {:} 차이: {:.2f}'.format(c,f,sf,sf-f))
    c+=3
