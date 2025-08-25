# finally: 오류 발생 여부가 상관없이 무조건 실행되는 블록
# 항상 마지막에 배치

try:
    f = open("test.txt", 'w') 
finally:
    f.close()
    print('file close')

print('프로그램이 정상적으로 종료되었습니다')
