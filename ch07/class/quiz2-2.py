# 응용

# Bus 클래스를 정의하고, 노선번호·승객수를 속성으로 넣어주세요
# 같은 버스에 승객을 여러 번 태우면 누적 인원이 합산됩니다
# 실행 결과:
# 9번 버스에 승객 10명이 탑승했습니다. (총 10명)
# 9번 버스에 승객 5명이 탑승했습니다. (총 15명)
# 111번 버스에 승객 3명이 탑승했습니다. (총 3명)
# 111번 버스에 승객 6명이 탑승했습니다. (총 6명)

class Bus:
    def __init__(self, route):
        self.route = route
        self.passengers = 0   # 처음 승객 수는 0명

    def take(self, num):
        self.passengers += num
        print(f"{self.route}번 버스에 승객 {num}명이 탑승했습니다. (총 {self.passengers}명)")

# 첫 번째 버스
b1 = Bus("9")
b1.take(10)   # 승객 10명 탑승
b1.take(5)    # 승객 5명 추가 탑승

# 두 번째 버스
b2 = Bus("111")
b1.take(3)   # 승객 3명 탑승
b1.take(6)    # 승객 6명 추가 탑승
