# 형변환
# 자료형을 다른 자료형으로 바꾸는 것

# 리스트나 문자열을 튜플로 변환할 수 있다

# list -> tuple
t1 = tuple([1, 2, 3])
print(t1, type(t1))

# string -> tuple
# 문자열을 한글자씩 잘라서 튜플로 변환
t2 = tuple('string')
print(t2, type(t2))

# 반대로 튜플을 리스트로 변환 가능
# tuple -> list
t = (1, 2, 3)
print(list(t))
