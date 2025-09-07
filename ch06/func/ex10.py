# 팩토리얼 재귀 함수 만들기
# 3! -> 3*2*1 = 6
# 5! -> 5*4*3*2*1 = 120

def factorial(n):
    if n == 1:   # 종료 조건 (재귀 탈출)
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(3))   # 120
print(factorial(5))   # 6
