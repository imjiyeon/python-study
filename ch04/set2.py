# 순서가 없기때문에 인덱싱을 지원하지 않는다
# set2[0] #에러남

# 인덱스를 사용하고 싶으면 set을 리스트나 튜플로 변환한다
s1 = set([1, 2, 3])
# 리스트로 변환
list = list(s1)
print(list)      # [1, 2, 3]
print(list[0])   # 1

# 튜플로 변환
tuple = tuple(s1)
print(tuple)      # (1, 2, 3)
print(tuple[0])   # 1


