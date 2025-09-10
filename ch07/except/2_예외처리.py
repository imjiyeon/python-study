# 예외 처리: 오류가 발생해도 프로그램이 멈추지 않고 계속 실행할 수 있음

# 예외 처리 구조
# try:
#     오류가 발생할 수 있는 코드
# except 발생오류 as 변수:
#     오류가 발생했을 때 실행할 코드
# try 블록에서 오류가 발생하면 except 블록이 실행됨

try:
    4 / 0
except ZeroDivisionError as e:
    print(e) # 오류메시지 출력

print('프로그램이 정상적으로 종료되었습니다')
