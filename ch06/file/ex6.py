# 파일 읽기모드로 열기
f = open("새파일.txt", 'r', encoding="utf-8")

# 파일의 내용을 하나의 문자열로 반환
data = f.read()

# 문자열을 공백 기준으로 잘라서 리스트로 변환
lis = data.split()
print(lis)

f.close()