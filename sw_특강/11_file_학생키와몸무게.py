'''
학과 : 컴퓨터 공학부
학번 : 202395032
이름 : 최민호

랜덤으로 10명의 학생의 키와 몸무게 생성하여 파일에 저장
'''

import random

f_name = list('김이박차성전남소조홍서남')
s_name = list('가나다라마바사아자차카타파하')

with open("info.txt", 'w') as file :
    for i in range(10) :
        name = random.choice(f_name) + random.choice(s_name) +random.choice(s_name) 
        weight = random.randrange(40,100)       #범위 지정
        height = random.randrange(140,200)
        
        file.write("{}, {}, {} \n" .format(name,weight,height))