# 메소드 오버라이딩

# 부모가 물려준 메소드가 자식의 비즈니스와 맞지 않을 때
# 재정의하여 사용한다

# 부모 클래스
class Person:
    def info(self):
        print("안녕하세요, 저는 사람입니다.")

# 자식 클래스
class Student(Person):
    def info(self):
        print("안녕하세요, 저는 학생입니다.")

# 객체 생성
s1 = Student()

# 부모가 물려준 메소드 호출
s1.info()   # 실제로는 자식 클래스에서 오버라이딩된 메서드가 실행됨
