'''
continue
'''
# 리스트의 값 10개 중에서 10보다 큰 수를 출력하세요.
numbers = [1,23,12,77,44,58,34,53,27]

print("리스트 값 중 10보다 큰 수 - 반복문 사용")

for i in numbers :
    if i >= 10 :
        print(i, end=', ')
        
print()

print("리스트 값 중 10보다 큰 수 - continue 사용")
for i in numbers :
    if i < 10 :
        continue
    print(i, end=', ')
    
print()

# 1~30 사이의 수 중에서 7의 배수만 출력하시오. continue 사용
# 7로 나누어서 나머지가 0인 수 
print("1~30 사이 중 7의 배수 출력")
num = list(range(1,31))

for i in num :
    if i % 7 != 0 :
        continue
    print(i, end=', ')
print()