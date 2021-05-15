from random import randint
li = []
for i in range(10):    
    l = randint(1,99)
    li.append(l)
print(li)

li.sort()
print(li)

li.sort(reverse=True)
print(li)






