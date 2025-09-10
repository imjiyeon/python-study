f = open('new.txt', 'w')
f.write('hello, world!')
f.close()

# with문으로 위 코드를 간단하게 작성

# with를 사용하면 블록이 끝날때 파일을 자동으로 닫아주기때문에
# close를 따로 호출할 필요가 없음

with open("new.txt", "w") as f:
    f.write("hello, world!")