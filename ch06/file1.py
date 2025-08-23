# 파일 생성하기
# f = open("새파일.txt", 'w')
# 작업이 끝나면 파일을 닫아야 메모리 낭비가 없음
# f.close()

# 파일에 내용 쓰기
# 지정한 경로에 파일이 없으면 새로 생성
# 파일이 이미 있으면 새로 덮어씀
# 인코딩을 지정하지 않으면 한글이 깨질 수 있음
# f = open("D:/workspace/python-study/ch06/새파일.txt", 'w')
f = open("D:/workspace/python-study/ch06/새파일.txt", 'w', encoding="utf-8")
for i in range(1, 11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()