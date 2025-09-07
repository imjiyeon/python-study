# 파일 쓰기 모드로 열기

# 'w' : 파일이 이미 있으면 덮어씀
f = open("file1.txt", 'w')

# 파일에 1부터 11까지 쓰기
for i in range(1, 11):
    # f.write(i) # 에러남. write는 문자열로 입력 가능. 숫자x
    # f.write(str(i)) # int->str
    # # 줄바꿈 없이 이어짐
    f.write(f"{i}\n") # 줄바꿈 추가

f.close()


