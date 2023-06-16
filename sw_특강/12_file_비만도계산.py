'''
학과 : 컴퓨터 공학부
학번 : 202395032
이름 : 최민호

키와 몸무게로 비만도 계산하기
'''

with open('info.txt', 'r') as file :
    for line in file :                       # strip 공백제거, split(",") 구분자
        (name, weight, height) = line.strip().split(",")
    
        if (not name) or (not weight) or (not height) :
            continue
    
        # 비만도 계산하기
        bmi = int(weight) / ((int(height) / 100) ** 2)
        if bmi >= 25 :
            result = '과체중'
        elif bmi >= 18.5 :
            result = '저체중'
        else :
            result = '정상'
            
        print("\n".join(['이름 : {}', '몸무게 : {}', '키 : {},', 'bmi : {:.2f}', '결과 : {}']).format(name,weight,height,bmi,result))
        print()