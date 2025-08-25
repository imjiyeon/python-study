# 비교 연산자

a = [1,2,3]
b = a
c = [1,2,3]

# 두 변수가 같은 객체를 가리키는지 확인
print(a is b)
print(a is not b)
# 두 변수의 값(내용)이 같은지 확인
print(a == b)
# 내용은 같지만 서로 다른 객체
print(a == c)
print(a is c)