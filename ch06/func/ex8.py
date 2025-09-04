# 변수의 유효 범위 (scope)

a = 1 # 전역 변수
def func(a): # 지역 변수
    a = a + 1

func(a)
print(a) # 여전히 1

# 잘못된 예제
# 함수 안에서 선언된 변수는 밖에서 쓸 수 없음
def func2(b):
    b = b + 1

func2(3)
# print(b) # 에러남