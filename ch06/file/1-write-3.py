# 파일 쓰기 모드로 열기

# 한글 입력시 인코딩 설정해야함
f = open("file2.txt", 'w', encoding="utf-8")

for i in range(1, 11):
    # 한글 쓰기 -> 깨짐
    f.write(f"{i}번째 줄입니다\n")

f.close()