# 메소드 오버라이드

# 부모가 물려준 메소드가 자식의 비즈니스와 맞지 않을 때
# 재정의하여 사용할 수 있다.

# 부모 클래스
class Animal:
    def bark(self):
        print("동물이 소리를 냅니다.")

# 자식 클래스
class Dog(Animal):
    def bark(self):
        print("멍멍!")

class Cat(Animal):
    def bark(self):
        print("야옹~")

dog = Dog()
# 오버라이드된 메서드가 실행됨
dog.bark() 

cat = Cat()
cat.bark()
