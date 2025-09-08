# 숫자를 입력 받아 짝수인지 홀수인지 알려주는 함수를 만드세요
# 예) 3 -> "홀수"
# 예) 10 -> "짝수"
def check_num(num):
    if num % 2 == 0:
        print("짝수")
    else:
        print("홀수")

check_num(3)   # 홀수
check_num(10)  # 짝수

# 값을 하나 입력 받아 타입이 str이면
# "문자입니다"를 출력하는 함수를 만드세요
# 타입이 str이 아니면 아무것도 출력되지 않습니다
# 예) 'abc' -> "문자입니다"
# 예) 100 -> x
# 예) True -> x

# 값을 하나 입력 받아 0보다 크면 "양수입니다"를 출력하는 함수를 만드세요
# 예) 10 -> "양수입니다"
# 예) -5 -> x
def check_int(value):
    if value > 0:
        print("양수입니다")

check_int(10)
check_int(-5)   

# 리스트를 입력받아 첫 번째 값을 반환하는 함수를 만드세요*
# 예) [10, 20, 30] -> 10
# 예) ["a", "b", "c"] -> "a"

def first_value(lis):
    return lis[0]

print(first_value([10, 20, 30]))  # 10
print(first_value(["a", "b", "c"]))  # a

# 문자열을 입력받아 길이를 반환하는 함수를 만드세요
# 예) "abc" -> 3
# 예) "hello" -> 5
def func(msg):
    return len(msg)

my_str1 = "abc"
result1 = func(my_str1)
my_str2 = "hello"
result2 = func(my_str1)

# 숫자를 입력받아 양수/음수/0을 판별하는 함수를 만드세요
# 예) 5 -> "양수"
# 예) -3 -> "음수"
# 예) 0 -> "0입니다"

