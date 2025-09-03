# 반복문을 사용해서 "하이" 3번 출력하기
i = 0
while i < 3:
    print("하이")
    i = i + 1

# 반복문을 사용해서 11부터 20까지 출력하세요
i = 11
while i <= 20:
    print(i)
    i += 1

# 반복문을 사용해서 11부터 20까지 합을 구하세요
num = 11   # 더할 숫자
sum = 0   # 합계를 저장할 변수

while num <= 20:
    sum = sum + num
    num += 1

print("11부터 20까지의 합:", sum)
