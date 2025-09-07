# 키보드로 값 입력받기
# 숫자를 입력받아 변수에 저장
# 터미널에서 숫자 입력 > 엔터
a = input()
print(a)

# 두 숫자를 입력받고 합 구하기
num1 = input("첫번째 숫자를 입력하세요: ")  
print(num1)

num2 = input("두번째 숫자를 입력하세요: ")  
print(num2)

sum = num1 + num2
# input은 문자열로 반환되어 문자열끼리 연결됨
print("두수의 합:", sum) # "1" + "2" => "12"

print(type(num1))

# int로 변환 후 더하기
sum = int(num1) + int(num2)
print("두수의 합:", sum)