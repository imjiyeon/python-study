# 파일에 새로운 내용 추가하기

# a: 추가 모드
f = open("D:/workspace/python-study/ch06/새파일.txt", 'a', encoding="utf-8")
for i in range(11, 20):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()

# with문 사용하기
# 자동 close
with open("new.txt", "w") as f:
    f.write("hello, world!")