# 화면에 출력하기
# print: 화면에 숫자,문자열,리스트 등을 출력

print(123)   # 숫자 출력
print("python")   # 문자열 출력
print([1, 2, 3])   # 리스트 출력

# 여러 문자열을 연결하여 출력
print("hello" "world")  
print("hello" + "world")
print("hello", "world") # 콤마를 쓰면 공백이 들어감

# print 함수는 출력 후 줄바꿈됨
# print(1, end='\n')
# end 옵션으로 출력 뒤에 올 문자를 지정할 수 있음
print(1)
print(2)
print(3)

# 여러 숫자를 한줄에 출력하기
# end 매개변수를 사용하여 줄바꿈 대신 공백 넣기
print(1, end=' ')
print(2, end=' ')
print(3, end=' ')
