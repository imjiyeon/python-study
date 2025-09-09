# 상속

# 부모 클래스
class Person:
    def info(self):
        print("안녕하세요, 저는 사람입니다.")

# 자식 클래스 (Person을 상속)
class Student(Person):
    pass

# 객체 생성
p1 = Person()
s1 = Student()

# 메서드 호출
p1.info()
s1.info()   # 부모 메서드를 그대로 상속받아 실행
