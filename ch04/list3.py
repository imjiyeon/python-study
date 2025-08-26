# 리스트 인덱싱

# 리스트의 각 요소는 인덱스 번호를 가지며,
# 인덱스 번호로 각 요소에 접근할 수 있다
# index: 0~2
lis = [1, 2, 3]
print(lis)

# 리스트의 첫번째 요소
print(lis[0])
# 리스트의 마지막 요소
print(lis[2])
print(lis[-1])

# 2번째 리스트
item = [1, "apple", 3, "banana"]
print(item)

# 첫번째 요소
print(item[0])
# 두번째 요소
print(item[1])
# 마지막 요소
print(item[3])
print(item[-1])

# 리스트 슬라이싱
# 리스트에서 일부분만 잘라내기
lis = [1,2,3,4,5]

# [시작위치:마지막위치]
print(lis[0:2]) # 처음부터 list[1] 까지 (2번은 포함안됨)
print(lis[:2]) # 처음부터 list[1] 까지
print(list[2:]) # list[2]부터 마지막까지

# 음수 인덱스
str = "hello!"
lis = list(str)
print(lis[0:3])
print(lis[-3:])
