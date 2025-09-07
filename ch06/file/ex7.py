# 파일에 새로운 내용 추가하기

# a: 이어 쓰기
f = open("file2.txt", 'a', encoding="utf-8")

for i in range(11, 20):
    data = f"{i}번째 줄입니다\n"
    f.write(data)

f.close()
