'''
리스트를 만들고, 반복문으로 출력하시오.
'''

import random

num = list(range(1,10))     # 1~9 까지 수를 num안에 저장
print("num1 : ", num)

for i in num :
    print(i, end=', ')
    
    
'''
1~100 사이의 정수중 램덤으로 10개의 수를 뽑아서 리스트에 저장하시오.
'''

num1 = []    # 빈 리스트 생성

for i in range(10) :
    num1.append(random.randint(1,100))
print("생성된 리스트 : " , num1)