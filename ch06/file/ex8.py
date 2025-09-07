# with문 사용하기

# with open .. as f를 사용하면
# 파일을 열고 블록이 끝날때 파일을 자동으로 닫아줌
# -> close를 따로 호출할 필요가 없음

with open("new.txt", "w") as f:
    f.write("hello, world!")