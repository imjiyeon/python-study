# 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b

# 순서대로 입력
result = sub(7, 3)
print(result)

# 매개변수 이름을 지정
# 순서와 상관없이 입력 간으
result = sub(b=5, a=3) 
print(result)
