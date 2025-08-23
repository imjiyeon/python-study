# 사용자 입력받기

# 사용자가 입력한 값을 a변수에 대입
a = input()

# 안내 문구와 함께 입력 받기
# 안내 문구가 프롬프트에 나타난다
number = input("숫자를 입력하세요: ")  
print(number)

# input은 입력되는 모든 것을 문자열로 취급한다
# number는 숫자가 아닌 문자열이다
print(type(number))