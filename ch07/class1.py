# 클래스 기본 구조
class Sample:
    pass

a = Sample()
b = Sample()

# 클래스 만들기
class Student:
    # 메서드의 첫 번째 매개변수 self
    # 자기 자신을 가리킴
    def go_school(self):
        print("학교에 갑니다.")

    def study(self):
        print("공부를 합니다.")

# 클래스로 객체 생성하기
student1 = Student()

# 클래스 객체 사용하기
student1.go_school()
student1.study()
