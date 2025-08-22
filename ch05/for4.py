total = 0
for num in range(1, 11):    # 1부터 10까지
    if num % 2 == 0:        # 짝수면 건너뛰기
        continue
    total += num

print("1부터 10까지의 홀수 합:", total)
