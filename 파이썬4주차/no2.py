import random



for i in range(5):
    hour = random.randint(35,50)
    money = 12000
    over = money*40
    cost = int((hour-40)*(money*1.5))
    
    if hour>=40:
        print('근로시간{}시간, 주급 {}'.format(hour,over+cost))
    else:
        print('근로시간{}시간, 주급 {}'.format(hour,hour*money))
        
