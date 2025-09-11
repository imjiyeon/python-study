#계산기

# 클래스 만들기
class Calc:
    # 클래스 변수 (공통 속성)
    type = "기본 계산기"

    def __init__(self, color):
        self.color = color    # 인스턴스 변수 (개별 속성)

    def add(self, a, b):
        print("결과:", a + b)

    def sub(self, a, b):
        print("결과:", a - b)

# 클래스로 객체 생성하기
calc = Calc('white')

# 클래스 객체 사용하기
calc.add(10, 5)
calc.sub(10, 5)

# 상속
# Calculator를 상속받아 확장
class newCalculator(Calc):
    calc_type = "공학용 계산기" 

    def mul(self, a, b):
        print("결과:", a * b)

    def div(self, a, b):
        if b != 0:
            print("결과:", a / b)
        else:
            print("0으로 나눌 수 없습니다.")

    # 부모 클래스의 메서드를 오버라이드
    def add(self, a, b):
        print("덧셈 결과:", a + b)

new = newCalculator('red')
new.add(10, 5)
new.sub(10, 5)
new.mul(10, 5)
new.div(10, 5)