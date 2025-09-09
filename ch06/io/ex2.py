# 화면에 출력하기
# print: 화면에 숫자,문자열,리스트 등을 출력하는 함수
print(123)        # 숫자 출력
print("python")   # 문자열 출력
print([1, 2, 3])  # 리스트 출력

# 여러 문자열을 연결하여 출력
print("hello" "world")  
print("hello" + "world")
print("hello", "world") # 콤마를 쓰면 공백이 들어감

# print 함수는 출력 후 줄바꿈됨
print(1) # 1을 출력하고 줄바꿈됨
print(2) 
print(3)
# 함수의 매개변수를 보면 end='\n' 라는 매개변수가 있음
# end 옵션은 출력 뒤에 올 문자를 지정하는 것

# end 매개변수를 줄바꿈 대신 공백으로 바꾸기
print(1, end=' ')
print(2, end=' ')
print(3, end=' ')
# 1 2 3 한줄에 출력됨
