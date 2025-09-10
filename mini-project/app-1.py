orders = []  # 모든 주문을 담는 리스트

def generate_order_no():
    if  len(orders) == 0:
        return 1
    else:
        # 음수 인덱스: -1은 리스트의 마지막 요소
        return orders[-1]["order_no"] + 1

# 주문번호는 생성
# 나머지는 입력받은 그대로
def create_order(name, product, count, price):
    order = {
        "order_no": generate_order_no(),
        "name": name,
        "product": product,
        "count": int(count),
        "price": int(price)
    }
    return order

def list_all():
    if len(orders) == 0:
        print("(주문 없음)")
    else:
        for o in orders:
            total = o["count"] * o["price"]
            print(
                "주문번호:", o["order_no"],
                "고객명:", o["customer"],
                "제품명:", o["product"],
                "수량:", o["count"],
                "단가:", o["price"],
                "총액:", total
            )

while True:
    print("\n1. 상품 주문하기")
    print("2. 전체 주문 이력 보기")
    print("3. 고객별 주문 통계")
    print("4. 끝내기")
    select = input("옵션을 선택하세요: ")

    if select == "1":
        name = input("고객명: ")
        product  = input("제품명: ")
        count    = input("제품수량: ")
        price    = input("제품가격: ")
        order = create_order(name, product, count, price)
        orders.append(order)
        print("주문이 완료되었습니다.")

    elif select == "2":
        list_all()

    elif select == "3":
        # 여기에 코드를 작성해주세요
        pass

    elif select == "4":
        print("프로그램을 종료합니다.")
        break

