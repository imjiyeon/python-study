# 1부터 20까지 더하다가
# 합이 100을 넘으면 while문 강제로 빠져나가기
num = 1
total = 0

while num <= 20:   # 1~20까지만 반복
    total += num
    if total > 100:   # 합이 100을 넘으면 종료
        break
    num += 1

print("마지막 더한 숫자:", num)
print("합계:", total)