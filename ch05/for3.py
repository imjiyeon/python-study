total = 0
for num in range(1, 21):   # 1부터 20까지 반복
    total += num
    if total > 100:        # 합이 100을 넘으면 종료
        break

print("마지막 더한 숫자:", num)
print("합계:", total)
