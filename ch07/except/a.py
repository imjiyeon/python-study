# 전역변수로 선언
f = None # 빈값
f = open('test.txt', 'w')
try:
    f = open('test.txt', 'r')
except FileNotFoundError as e:
    print(e)
finally:
    if f == None:
        print('파일이 존재하지 않습니다')
    else:
        print('파일을 닫았습니다')
        f.close()
