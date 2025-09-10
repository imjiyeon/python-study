# 응용

# Account 클래스를 정의하고, 
# deposit(amount), withdraw(amount) 메서드를 만들어주세요
# 객체를 생성하고 입금과 출금을 실행하세요
# 단, 출금시 예금이 부족하면 "잔액이 부족합니다"를 출력하세요
# 실행 결과:
# 10000원 입금 완료. 현재 잔액: 10000원
# 3000원 출금 완료. 현재 잔액: 7000원
# 잔액이 부족합니다.

class Account:
    balance = 0  # 초기 잔액 0

    def deposit(self, amount):
        self.balance += self.balance + amount
        print(f"{amount}원 입금 완료. 현재 잔액: {self.balance}원")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= self.balance - amount
            print(f"{amount}원 출금 완료. 현재 잔액: {self.balance}원")
        else:
            print("잔액이 부족합니다.")

a = Account()
a.deposit(10000)
a.withdraw(3000)
a.withdraw(8000)