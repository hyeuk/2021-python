data = [[1,2,3],
        [4,5,6],
        [7,8,9]]


a1 = data[0][0] 
a2 = data[0][1] 
a3 = data[0][2] 
a = a1+a2+a3

b1 = data[1][0] 
b2 = data[1][1] 
b3 = data[1][2] 

b = b1+b2+b3

c1 = data[2][0] 
c2 = data[2][1] 
c3 = data[2][2] 

c = c1+c2+c3

rsum = []
rsum.append(a)
rsum.append(b)
rsum.append(c)

d = a1+b1+c1
e = a2+b2+c2
f = a3+b3+c3

csum = []
csum.append(d)
csum.append(e)
csum.append(f)

print(rsum)
print(csum)



