# 묵시적 형변환
# 묵시적 형변환이란 정수(int)와 실수(float)를 함께 계산할 때,
# 정수가 자동으로 실수로 변환되는 것

a=4.5
b=2

# b는 int지만 계산할 때 자동으로 float로 변환됨
print(a/b, type(a/b))

# type: 자료형 확인
print(type(a))

# isinstance: 해당 타입이 맞는지 확인
print(isinstance(a, float))
print(isinstance(a, (int, float)))