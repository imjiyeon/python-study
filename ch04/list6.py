# 리스트 관련 함수

# 리스트 정렬
lis = [1,4,3,2]
lis.sort()
print(lis)

# 리스트 뒤집기
lis2 = ['a','c','b']
lis2.reverse()
print(lis2)

# 인덱스 반환
# index(value) -> index
lis3 = ['a','b','c']
index = lis3.index('a')
print(index)

# 존재하지 않는 값을 찾으면 에러남
# index = lis2.index('e') 

# 리스트에 포함된 특정요소의 개수 세기
lis4 = [1,2,3,1]
cnt = lis4.count(1)
print(cnt)