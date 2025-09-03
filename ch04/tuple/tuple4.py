# 튜플 값 분리하기
t1 = (4, 5, 6)
a, b, c = t1
print(a, b, c)

# 변수 값 교환하기
a, b = 1, 2
print(a, b)

b, a = a, b
print(a, b)

# *rest : 나머지 값을 모아서 리스트에 담기
values = (1, 2, 3, 4, 5)
a, b, *rest = values
print(a, b, rest)
