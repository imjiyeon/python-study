# 재귀함수로 다운로드 폴더 내부에 파일까지 모두 출력하기

import os

def list_files(path, indent=0):
    items = os.listdir(path)
    for item in items:
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):   # 폴더면 재귀 호출
            print("  " * indent + "[DIR] " + item)
            list_files(full_path, indent + 1)
        else:                          # 파일이면 출력
            print("  " * indent + item)

# 실행
path = "C:/Users/imjiyeon/Downloads"
list_files(path)
