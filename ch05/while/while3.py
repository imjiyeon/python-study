# 숫자 1부터 10까지 합 구하기
sum = 0
sum = sum + 1
sum = sum + 2
sum = sum + 3
sum = sum + 4
sum = sum + 5
sum = sum + 6
sum = sum + 7
sum = sum + 8
sum = sum + 9
sum = sum + 10
print("1부터 10까지의 합:", sum)

# 반복문으로 합 구하기
num = 1   # 더할 숫자
sum = 0   # 합계를 저장할 변수

while num <= 10:
    sum = sum + num
    num += 1

print("1부터 10까지의 합:", sum)
