# 두 수를 곱하는 람다 함수를 작성하세요
add = lambda a, b: a * b

print(add(3, 7))  # 21

# 이름과 인사말을 받아 '이름 + 인사말' 형태로 출력하는 람다 함수를 작성하세요
greet = lambda name, msg: name + " " + msg
print(greet("둘리", "안녕"))  # 둘리 안녕


# 숫자를 입력받아 "홀수" 또는 "짝수"를 출력하는 람다 함수를 작성하세요
odd_even = lambda x: "짝수" if x % 2 == 0 else "홀수"

print(odd_even(3))  # 홀수
print(odd_even(4))  # 짝수
