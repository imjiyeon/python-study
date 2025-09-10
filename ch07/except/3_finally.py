# finally: 오류 발생 여부와 상관없이 항상 실행되는 블록
# 항상 마지막에 배치

# 보통 파일 닫기 같은 작업에 사용됨
try:
    f = open("test.txt", 'w') 
finally:
    f.close()
    print('file close')

print('프로그램이 정상적으로 종료되었습니다')
