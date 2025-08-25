# 오류가 발생해도 프로그램이 멈추지 않고 계속 실행되도록
# 예외 처리를 할수 있다

try:
    4 / 0
except ZeroDivisionError as e:
    print(e) # 오류메시지 출력

print('프로그램이 정상적으로 종료되었습니다')

# try:
#     오류가 발생할 가능성이 있는 코드 작성
# except 발생오류 as 변수:
#     오류가 발생했을 떄 실행할 코드 작성
# try 블록에서 오류가 발생하면 except 블록이 실행된다


