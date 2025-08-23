# 출력하기
# print: 프롬프트에 문자열을 출력하는 함수

a = 123
print(a)   # 숫자 출력

a = "Python"
print(a)   # 문자열 출력

a = [1, 2, 3]
print(a)   # 리스트 출력

# 문자열 연결
print("life" "is" "too short")  
print("life" + "is" + "too short")

# 공백 추가
print("life", "is", "too short")

# 파이썬의 print는 기본적으로 마지막에 줄바꿈됨
# 기본값은 print(1, end='\n')
print(1)
print(2)
print(3)

# 한줄에 출력
# end라는 매개변수를 사용하여 줄바꿈 대신 공백 하나를 넣는 것
print(1, end=' ')
print(2, end=' ')
print(3, end=' ')
