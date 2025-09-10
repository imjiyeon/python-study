# 응용

# Coffee 클래스를 정의하고, 이름·주문건수 속성을 넣어주세요
# 같은 커피를 여러 번 주문하면 누적 잔수가 합산됩니다
# # 실행 결과:
# 아메리카노를 2잔 추가 주문했습니다. (총 2잔)
# 아메리카노를 1잔 추가 주문했습니다. (총 3잔)
# 카페라떼를 3잔 추가 주문했습니다. (총 3잔)
# 카페라떼를 2잔 추가 주문했습니다. (총 5잔)

class Coffee:
    def __init__(self, name):
        self.name = name
        self.count = 0   # 처음 주문 건수는 0잔

    def order(self, num):
        self.count += num
        print(f"{self.name}를 {num}잔 추가 주문했습니다. (총 {self.count}잔)")

# 첫 번째 커피 주문
c1 = Coffee("아메리카노")
c1.order(2)   # 아메리카노 2잔
c1.order(1)   # 아메리카노 1잔 추가

# 두 번째 커피 주문
c2 = Coffee("카페라떼")
c2.order(3)   # 카페라떼 3잔
c2.order(2)   # 카페라떼 2잔 추가
