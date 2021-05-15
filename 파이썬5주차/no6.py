m = [[1,2],[3,4],[5,6],[7,8]]

print('원 행렬(m) 출력:')
for i in range(len(m)):
    print('{:d} {:d}'.format(m[i][0],m[i][1]))
    
    

print()
print('전치 행렬 출력:')
for i in range(len(m)-2):
    print('%d %d %d %d'%(m[0][i],m[1][i],m[2][i],m[3][i]))
    
    
                
