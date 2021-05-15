m = [[1,2],[3,4],[5,6],[7,8]]

print('트렌스포즈를 컴프리헨션으로 만들어 그대로 출력')
transpose = [[row[i] for row in m] for i in range(len(m[0]))]
print(transpose)
print()

print('트렌스포즈를 for문으로 출력')
for i in range(len(transpose)):
    print(transpose[i][0],transpose[i][1],transpose[i][2],transpose[i][3])
    

