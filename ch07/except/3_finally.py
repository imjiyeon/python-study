f = None
try:
    f = open('test.txt', 'r')
except FileNotFoundError as e:
    print(e)
finally:
    if f != None:
        f.close()
        print('파일을 닫습니다')
    else:
        print('파일이 존재하지 않습니다')