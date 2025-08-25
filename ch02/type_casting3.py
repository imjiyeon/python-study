# 묵시적 형변환

a=4.5
b=2
print(type(a), type(b))
print(a/b, type(a/b))

# b는 정수지만 계산할때 묵시적으로 float로 변환됨

# type: 정확한 자료형을 반환
print(type(a))

# isinstance: 지정한 타입이 맞는지 확인
print(isinstance(a, int))
print(isinstance(a, float))
print(isinstance(a, (int, float)))