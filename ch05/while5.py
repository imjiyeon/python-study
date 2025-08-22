# 1부터 10까지 더하는데, 홀수만 더하기
# while문의 맨 처음으로 돌아가기

num = 1
total = 0

while num <= 10:
    if num % 2 == 0:   # 짝수일 때는 건너뛰기
        num += 1
        continue
    total += num
    num += 1

print("1부터 10까지의 홀수 합:", total)
