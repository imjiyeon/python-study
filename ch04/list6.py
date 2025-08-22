# 리스트 관련 함수

# 리스트 정렬
list = [1,4,3,2]
list.sort()
print(list)

# 리스트 뒤집기
list2 = ['a','c','b']
list2.reverse()
print(list2)

# 인덱스 반환
# index(value) -> index
list3 = ['a','b','c']
index = list3.index('a')
print(index)

# 존재하지 않는 값을 찾으면 에러남
# index = list2.index('e') 

# 리스트에 포함된 특정요소의 개수 세기
list4 = [1,2,3,1]
cnt = list4.count(1)
print(cnt)