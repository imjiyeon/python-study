# 두 숫자를 입력받아 곱셈 결과를 출력하세요
# 예) 5,10 => 50
num1 = input("첫번째 숫자를 입력하세요: ")
num2 = input("두번째 숫자를 입력하세요: ")
result = int(num1) * int(num2)
print("결과:", result)

# 사용자로부터 이름과 나이를 입력받아 자기소개를 출력하세요
# 예) 둘리, 7 => "둘리님의 나이는 7세입니다"

name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")

print(f"{name}님의 나이는 {age}세입니다")

# 사과 가격과 수량을 입력 받아 총 가격 계산하세요
# 예) 사과가격: 1500, 사과개수: 5 => 7500원
price = int(input("사과 1개의 가격을 입력하세요: "))
count = int(input("구매한 사과 개수를 입력하세요: "))

total = price * count
print("총 가격은", total, "원 입니다")
