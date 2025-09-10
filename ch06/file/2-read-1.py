# 파일 읽기모드로 열기
# r: 읽기 모드
f = open("file1.txt", 'r', encoding="utf-8")

# 파일 내용을 줄 단위로 읽어 리스트로 반환
lines = f.readlines()

# 리스트에 담긴 각 줄을 출력
for line in lines:
    # print(line) # line에 이미 줄바꿈이 포함되어 있어서 두번 줄바꿈됨
    print(line, end='')

f.close()
