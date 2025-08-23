# 함수의 여러 가지 형태

# 입력값 있고, 리턴값도 있는 함수
def add(a, b):
    result = a + b
    return result

a = add(3, 4)
print(a)

# 입력값 없고, 리턴값 있는 함수
def say():
    return 'Hi'

a = say()
print(a)

# 입력값 있고, 리턴값 없는 함수
def add(a, b):
    print(a, b, "의 합은:", a+b)

add(3, 4)

a = add(3, 4)
print(a)

# 입력값 없고, 리턴값도 없는 함수
def say():
    print('Hi')

say()
