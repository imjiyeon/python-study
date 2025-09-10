# 다운로드 폴더에 있는 파일 목록 읽기

import os

# Downloads 경로 설정
# 역슬래시\를 슬래시/로 변경
path = "C:/Users/imjiyeon/Downloads"

# 파일 목록 가져오기
files = os.listdir(path)

# 출력
for f in files:
    print(f)
