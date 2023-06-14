'''
사용자가 0을 입력할 떄 까지
사용자가 원하는 구구단 출력하기

[문제 분석]
무한반복 - while Ture
사용자가 0을 입력 할 떄까지 계속 단을 입력 받는다.

사용자가 0을 입력 했는지 아닌지를 판단.

구구단은 곱하는 수가 1~9까지 1씩 증가한다.
'''

# 알고리즘
# 1. 무한 반복한다.
#   1-1) 단을 입력 받는다.
#   1-2) 입력 값이 0인가?
#       a. 프로그램 종료 (braak)
#   1-3) 곱하는 수를 1부터 10까지 반복하면서 
#       a.구구단을 출력한다.
# 2. "구구단 종료" 출력한다.

while True :
    dan = int(input("단을 입력 하세요. (종료키 : 0) "))
    if dan == 0 :
        break
    for i in range(1,10) :
        print(dan,"x",i,"=",dan*i)
print("구구단 종료")


while True :
    dan = int(input("단을 입력 하세요. (종료키 : 0) "))
    if dan == 0 :
        # print("구구단 종료")
        break
    su = 1   # 반복의 초기값
    while su <= 9 :   # 조건식
        print("{} x {} = {}" .format(dan,su,dan*su))
        su += 1   # 증감식
print("구구단 종료")