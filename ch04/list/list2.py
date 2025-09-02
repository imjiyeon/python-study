# 리스트 인덱싱

# 리스트의 각 요소는 인덱스 번호로 접근할 수 있다
lis = ['a', 'b', 'c']
print(lis)

# 첫번째 요소
print(lis[0])
# 두번째 요소
print(lis[1])
# 세번째 요소
print(lis[2])
# 마지막 요소
print(lis[-1])

# 리스트 슬라이싱
lis = ['a','b','c','d','e']

# [시작위치:마지막위치]
print(lis[0:2]) # 처음부터 list[1] 까지 (2번은 포함안됨)
print(lis[:2]) # 처음부터 list[1] 까지
print(lis[2:]) # list[2]부터 끝까지

