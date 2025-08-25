# 상속받고 자식 클래스 확장

# 부모 클래스
class Person:
    def info(self):
        print("안녕하세요, 저는 사람입니다.")

# 자식 클래스
class Student(Person):
    def study(self):
        print("공부를 합니다.")

# 객체 생성
s1 = Student()

# 부모가 물려준 메소드 사용
s1.info()   

# 자식 클래스에서 확장한 메서드 사용
s1.study()

# Person을 상속받는 두번째 자식 클래스
# 자식 클래스 Teacher
class Teacher(Person):
    def teach(self):
        print("학생을 가르칩니다.")

# 객체 생성
t1 = Teacher()

# 부모가 물려준 메소드 사용
t1.info()

# 자식 클래스 확장 메서드 사용
t1.teach()