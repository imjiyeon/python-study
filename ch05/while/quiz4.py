# 다음 리스트를 만들고,
# while 반복문으로 요소를 하나씩 출력하세요.
# 단, 음수를 만나면 continue를 사용해 건너뛰세요
lis = [100,77,-5,10]
i = 0
while i < 4:
    if lis[i] < 0:
        i += 1
        continue
    print(lis[i])
    i += 1

# 다음과 같이 리스트를 만들고 
# 반복문으로 요소를 하나씩 출력하다가
# 단, 77을 만나면 break를 사용해 반복문을 종료하세요
lis = [100,77,-5,10]
i = 0
while i < 4:
    if lis[i] == 77:
        i += 1
        break
    print(lis[i])
    i += 1


