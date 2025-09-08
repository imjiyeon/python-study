# 리스트를 입력받아 리스트 안의 숫자를 모두 더해 합을 반환하는 함수를 만드세요
# 예) [1, 2, 3, 4, 5] -> 15
# 예) [10, 20, 30] -> 60
def sum_list(numbers):
    total = 0
    for n in numbers:   
        total = total + n     
    return total

print(sum_list([1, 2, 3, 4, 5]))  # 15
print(sum_list([10, 20, 30]))     # 60

# 단을 입력 받아 구구단을 출력하는 함수를 만드세요
# 예) 3 ->
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
def gugu(n):
    for i in range(1, 10):
        print(f"{n} x {i} = {n*i}")

gugu(3)

# 리스트를 입력받아 그 안에 문자열(str) 자료형이 몇 개인지 세는 함수를 만드세요
# 예) [1, "apple", 3.5, "banana", 10, "hi"] -> 3

def count_str(lis):
    cnt = 0
    for item in lis:
        if type(item) == str:
            cnt = cnt + 1
    return cnt

print(count_str([1, "apple", 3.5, "banana", 10, "hi"]))  # 3
print(count_str(["a", "b", "c"]))  # 3
print(count_str([1, 2, 3]))        # 0
