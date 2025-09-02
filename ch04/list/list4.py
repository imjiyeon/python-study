# 리스트 CRUD 함수

lis = [1,2,3]

# 리스트 길이 확인
length = len(lis)
print(length)

# append : 새로운 요소를 맨뒤에 추가
lis.append(4)
print(lis)

# insert : 특정 위치에 새로운 요소를 추가
# 입력값: 특정위치,새로운값
lis.insert(0, 4) # 0번째 자리에 4를 삽입
print(lis)

# 값 수정
lis[2] = 4
print(lis)

# 값 삭제
del lis[1] # 인덱스 사용
print(lis)

# 값으로 삭제
lis.remove(3)
print(lis)

# pop : 마지막 요소 꺼내면서 삭제
last = lis.pop()
print(lis, last)
