'''
학생 이름과 점수를 입력 받아 리스에 저장하고,
학생 점수의 촘점과 평균을 출력하시오.
'''

# [알고리즘]
# 0. 빈 학생 리스트 생성
# 1. 학생 수 입력받기
# 2. 학생 수 만큼 반복하면서 
#   2-1) 학생 이름과 점수 저장. - 리스트
#   2-2) 점수 합계 계산
# 3. 리스트에 저장된 학생 정보 출력
# 4. 총점과 평균 출력

student = []
sum = 0

num = int(input("학생 수를 입력하세요. : "))

for i in range(num) :
    print("<", i+1, "번째 학생 정보 입력 >")
    name = input("학생 이름 입력 : ")
    score = int(input("%s의 점수 입력 : " %name))
    student.append([name,score])
    sum = sum + score
    
for info in student :
    print("이름 : ", info[0], "점수 : ", info[1])
print("학생 점수 합계 : ", sum)
print("학생 점수 평균 : {:.2f}" .format(sum/num))