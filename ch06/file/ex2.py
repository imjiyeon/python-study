# 파일 읽기

# r: 읽기 모드
# readlines: 파일 내용을 줄 단위로 읽어 리스트로 반환
f = open("D:/workspace/python-study/ch06/새파일.txt", 'r', encoding="utf-8")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# read: 파일의 내용을 하나의 문자열로 반환
f = open("D:/workspace/python-study/ch06/새파일.txt", 'r', encoding="utf-8")
data = f.read()
print(data)
f.close()
