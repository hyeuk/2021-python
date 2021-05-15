from random import randint

ran = []

for i in range(0,10):
    r = randint(1,99)
    ran.append(r)
print('리스트:',ran)

tup = tuple(ran)
print('튜플:',tup)

s_tup =sorted(tup)
print('튜플 정렬된 리스트:',s_tup)

print()

mn = min(tup)
mx = max(tup)
sm = sum(tup)
avg = sm / 10

print('합:{:d}, 항목수:{:d}\n최대:{:d}, 최소:{:d}, 평균:{:.2f}'.format(sm,len(tup),mx,mn,avg))

    
