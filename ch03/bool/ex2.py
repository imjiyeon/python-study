# 논리연산자로 조건식 만들기

# and 연산자 : 양쪽 모두 참일때만 결과가 참
print(True and True) 
print(True and False)  

# or 연산자 : 한쪽이라도 참이면 결과가 참
print(True or False)
print(False or False)

# not 연산자 : 참/거짓을 반대로 바꿈
print(not True)

# 변수를 사용해 조건식 만들기
age = 20
money = 10000
# 나이가 19살 이상이고 소지금이 25000원 이상이면 참(true)
print(age >= 19 and money >= 25000)