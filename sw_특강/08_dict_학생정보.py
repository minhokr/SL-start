'''
학과 : 컴퓨터 공학부
학번 : 202395032
이름 : 최민호

학생 정보를 사전에 저장하고, (학번, 이름)
특정 학생의 정보(학번)를 입력하여 학생을 찾아주세요.
'''

# 알고리즘
# 1. 학생 정보 저장 사전 만들기 - 빈 사전 만들기
# 2. 학생 정보 입력 - 사전에 저장 (z 키를 누르면 종료 - 무한반복)
# 3. 학번으로 검색하여 학생 찾기 (학번이 빈칸이면 검색 종료 - 무한반복)

student = {}

while True:
    student_id = input("학번을 입력하세요 (종료하려면 'z' 입력): ")
    if student_id == 'z':                                                              
        break 
    student_name = input("이름을 입력하세요: ")                      

    student[student_id] = student_name
print('입력되 학생 정보')
print('',student)
while True:
    student_ward = input("검색을 원하는 학생 학번 입력 (종료: enter): ")                  
    if student_ward == '':                                                                                              
        print("프로그램을 종료합니다.")
        break 
    
    else:
        if student_ward in student:                                                    
            print("== 검색한 학생 정보 ==")                                            
            print("학번 : ", student_ward,"이름 : ", student.get(student_ward))
        else: 
            print("검색한 학생이 존재하지 않습니다.")
