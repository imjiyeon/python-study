# 파일 내용 읽어오기

# 파일이름, 모드
# 파일에 한글이 있으면 인코딩 추가
f = open('file2.txt','r', encoding='utf-8')

# read 함수로 내용 읽어오기
# readlines는 리스트로 반환
lis = f.readlines()

print(lis)

# # 내용을 한줄씩 출력
# for line in lis:
#     print(line)