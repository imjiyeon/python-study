# 다음과 같이 리스트를 만들고 
# for문으로 모든 요소를 더해서 합을 구하세요
nums = [10, 20, 30, 40, 50]
total = 0
for n in nums:
    total += n
print("합:", total)

# 1부터 100까지 숫자 중에서 3의 배수의 합을 구하세요
total = 0
for i in range(1, 101):
    if i % 3 == 0:
        total += i
print("3의 배수 합:", total)