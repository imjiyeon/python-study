# 반복문을 사용해서 11부터 20까지 합을 구하세요
num = 11   # 더할 숫자
sum = 0   # 합계를 저장할 변수

while num <= 20:
    sum = sum + num
    num += 1

print("11부터 20까지의 합:", sum)
