# 변수가 필요하지 않을 때는 _로 표시

# 안녕하세요 10번 출력
for _ in range(10):
    print("Hello, world!")

# 숫자 3번 입력 받기
total = 0
for _ in range(3):
    num = int(input())
    total = total + num

print("합계:", total)