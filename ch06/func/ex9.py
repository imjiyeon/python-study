# 익명(람다) 함수
# 함수를 짧게 만들 때 사용

# 변수 = lambda 매개변수: 코드
add = lambda a, b: a + b

# 변수를 함수이름처럼 사용함
result = add(3, 4)
print(result)

# 아래와 같은 함수
def add(a, b):
    return a + b

result = add(3, 4)
print(result)

# 정렬에 람다 함수 사용하기
strings = ["foo", "card", "ba", "aaa", "abab"]
result = strings.sort(key=lambda x: len(x))
print(strings)
