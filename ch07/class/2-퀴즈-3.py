# 응용

# Subway 클래스를 정의하고, 노선이름·승객수·요금을 속성으로 넣어주세요
# 승객이 탑승할 때마다 인원수가 누적되고 요금도 합산됩니다
# 1인당 요금: 1500원
# 실행 결과:
# 2호선에 승객 5명이 탑승했습니다. (총 5명, 요금 7500원)
# 2호선에 승객 3명이 탑승했습니다. (총 8명, 요금 12000원)
# 9호선에 승객 10명이 탑승했습니다. (총 10명, 요금 15000원)
# 9호선에 승객 4명이 탑승했습니다. (총 14명, 요금 21000원)

class Subway:
    def __init__(self, line, fare=1500):
        self.line = line
        self.fare = fare         # 1인당 기본 요금
        self.passengers = 0      # 승객 수
        self.total_fare = 0      # 누적 요금

    def take(self, num):
        self.passengers += num
        self.total_fare += num * self.fare
        print(f"{self.line}에 승객 {num}명이 탑승했습니다. (총 {self.passengers}명, 요금 {self.total_fare}원)")

# 첫 번째 지하철
s1 = Subway("2호선")
s1.take(5)   # 승객 5명
s1.take(3)   # 승객 3명 추가

# 두 번째 지하철
s2 = Subway("9호선")
s2.take(10)  # 승객 10명
s2.take(4)   # 승객 4명 추가
