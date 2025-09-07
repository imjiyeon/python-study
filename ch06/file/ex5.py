# 파일 읽기모드로 열기
f = open("file2.txt", 'r', encoding="utf-8")

# 파일의 내용을 하나의 문자열로 반환
data = f.read()
print(data)

f.close()
