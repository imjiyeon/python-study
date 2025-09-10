# 기본

# Book 클래스를 정의하고, 제목·저자·가격을 속성으로 넣어주세요
# 책 객체를 3권 만들어 출력하세요
# 실행 결과:
# 파이썬 기초 15000
# 자료구조 18000
# 알고리즘 20000
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

b1 = Book("파이썬 기초", "홍길동", 15000)
b2 = Book("자료구조", "김철수", 18000)
b3 = Book("알고리즘", "이영희", 20000)

print(b1.title, b1.price)
print(b2.title, b2.price)
print(b3.title, b3.price)

# Car 클래스를 정의하고, 모델명·색상·연식을 속성으로 넣어주세요
# 자동차 객체를 2대 만들어 출력하세요
# 실행 결과:
# 소나타 흰색
# 아반떼 검정
class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

c1 = Car("소나타", "흰색", 2020)
c2 = Car("아반떼", "검정", 2022)

print(c1.model, c1.color)
print(c2.model, c2.color)

# Order 클래스를 정의하고, 주문번호·상품명·수량을 속성으로 넣어주세요
# 주문 객체를 2개 만들어 출력하세요
# 실행 결과:
# 노트북 1
# 마우스 3

class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity

o1 = Order(101, "노트북", 1)
o2 = Order(102, "마우스", 3)

print(o1.product, o1.quantity)
print(o2.product, o2.quantity)
