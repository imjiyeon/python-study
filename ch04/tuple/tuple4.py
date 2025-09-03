# 튜플 값 분리하기
t1 = (1, 2, 3)
a, b, c = t1 # 튜플을 변수에 순서대로 나눠 담기
print(a, b, c)

# *rest : 나머지 값을 모아서 리스트에 담기
values = (1, 2, 3, 4, 5)
a, b, *rest = values # ab에 12를 담고 나머지는 rest에
print(a, b, rest)
