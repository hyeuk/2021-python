h,w = input('당신의 키(cm)와 몸무게(kg)는? >>').split()
height = float(h)
weight = float(w)

bmi =weight / (height/100)**2

if bmi >=40:
    print('키: {}(cm), 몸무게: {}(kg)\nBMI: {:.1f} {}'.format(height,weight,bmi,'고도 비만'))
elif bmi >=35:
    print('키: {}(cm), 몸무게: {}(kg)\nBMI: {:.1f} {}'.format(height,weight,bmi,'중등도 비만'))    
elif bmi >=30:
    print('키: {}(cm), 몸무게: {}(kg)\nBMI: {:.1f} {}'.format(height,weight,bmi,'비만'))
elif bmi >=25:
    print('키: {}(cm), 몸무게: {}(kg)\nBMI: {:.1f} {}'.format(height,weight,bmi,'과제중'))
elif bmi >=18.5:
    print('키: {}(cm), 몸무게: {}(kg)\nBMI: {:.1f} {}'.format(height,weight,bmi,'정상'))
else:
    print('키: {}(cm), 몸무게: {}(kg)\nBMI: {:.1f} {}'.format(height,weight,bmi,'저체중'))
    
    
