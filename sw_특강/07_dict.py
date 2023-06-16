'''
학과 : 컴퓨터 공학부
학번 : 202395032
이름 : 최민호

사전 : 키와 값으로 이루어 짐.
키는 중복 불가
'''

list = [[1,'하나'],[2,'둘'],[3,'셋']]
dict1 = dict(list)

print("리스트 : ", list)
print("사전 : ", dict1)

# 사전 생성
dict2 = {'제목' : '어벤져스 엔드게임' , '장르' : '히어로무비'}
print("영화 : ", dict2)

# 특정 키의 값을 출력
# 키 값은 리스트의 [] 사용, dict2{'제목'} = 오류발생
print("영화 제목 : ", dict2['제목'])
print("영화 장르 : ", dict2['장르'])

# 영화 감독 이름 추가 - 딕셔너리 내부 값에 리스트로 자료 추가
print("딕셔너리에 요소 추가")
dict2['감독'] = ['안소니 루소', '주 루소']
print("영화 : ", dict2)

# 출연진 추가
dict2['출연진'] = ['아이언맨', '나뭇가지', '스파이더맨', '너구리']
print("영화 : ", dict2)
print("영화 출연진 : ", dict2['출연진'])

# 장르 변경
dict2['장르'] = 'SF'
print("영화 : ", dict2)

# 다음 코드의 결과를 작성하시오.
dict2['출연진'][1] = '타노스'
print('영화 출연진 : ', dict2['출연진'])

print("특별 캐스팅 : ", dict2['출연진'][1])

# 출연진 삭제
del dict2['출연진']
print("영화 : ", dict2)

# 빈 사전 생성
student = {}
print("학생 추가 전 : ", student)

student['학과'] = '컴퓨터공학부'
student['학번'] = '202395032'
student['이름'] = '최민호'

print('학생 추가 후 : ', student)

# 딕셔너리에 키가 있는지 확인
key = input('찾고 싶은 키 입력 : ')
if key in student :
    print(student[key])
else :
    print('존재 하지 않는 키 입니다.')