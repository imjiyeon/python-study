# 상속

# 1.
# Animal 클래스를 정의하고, eat() 메서드를 만들어주세요
# Dog 클래스는 Animal을 상속받아 bark() 메서드를 추가합니다
# 실행 예시:
# 동물이 먹습니다.
# 강아지가 짖습니다.

class Animal:
    def eat(self):
        print("동물이 먹습니다.")

class Dog(Animal):
    def bark(self):
        print("강아지가 짖습니다.")

a = Animal()
a.eat()

d = Dog()
d.eat()   # 부모 메서드 사용
d.bark()  # 자식만의 메서드

# 2.
# Book 클래스를 정의하고, read() 메서드를 만들어주세요
# EBook 클래스는 Book을 상속받아 download() 메서드를 추가합니다
# 실행 예시:
# 책을 읽습니다.
# 전자책을 다운로드합니다.

class Book:
    def read(self):
        print("책을 읽습니다.")

class EBook(Book):
    def download(self):
        print("전자책을 다운로드합니다.")

b = Book()
b.read()

e = EBook()
e.read()       # 부모 메서드
e.download()   # 자식 메서드

# 3.
# Monster 클래스를 정의하고, attack() 메서드를 만들어주세요
# Slime 클래스는 Monster를 상속받아 jump_attack() 메서드를 추가합니다
# 실행 예시:
# 몬스터가 기본 공격을 합니다!
# 슬라임이 점프해서 몸통 박치기를 합니다!

class Monster:
    def attack(self):
        print("몬스터가 기본 공격을 합니다!")

class Slime(Monster):
    def jump_attack(self):
        print("슬라임이 점프해서 몸통 박치기를 합니다!")

m = Monster()
m.attack()

s = Slime()
s.attack()       # 부모 메서드
s.jump_attack()  # 자식 메서드


