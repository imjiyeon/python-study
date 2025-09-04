# 두 개의 숫자를 입력받아, 첫 번째 수에서 두 번째 수까지의 합을 반환하는 함수를 작성하고 호출하세요
# 예) 입력: 5, 10 → 반환: 5+6+7+8+9+10 = 45

def hap(n1, n2):
    result = 0 
    for i in range(n1, n2 + 1):  # n1부터 n2까지 반복
        result = result + i
    return result

sum = hap(5, 10)

print("5부터 10까지의 합:", sum)

# 두 개의 숫자를 입력받아, 첫 번째 수에서 두 번째 수를 뺀 결과를 반환하는 함수를 작성하고 호출하세요
# 단, 첫 번째 수가 두 번째 수보다 작으면 -999를 반환하세요

# 예)
# 입력: 20, 10 → 반환: 10
# 입력: 10, 20 → 반환: -999

def sub(n1, n2):
    if n1 < n2:
        return -999
    
    result = n1 - n2
    return result

result = sub(10, 20)
print("10 - 20 =",result)
