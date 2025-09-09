# 클래스변수와 인스턴스 변수

class Student:
    # 클래스 변수 (모든 객체가 공유)
    school_name = "연희직업전문학교"

    def __init__(self, student_id, name):
        # 인스턴스 변수 (객체마다 독립적)
        self.student_id = student_id
        self.name = name

# 객체 생성
s1 = Student(101, "둘리")
s2 = Student(102, "도우너")

# 클래스 변수는 모든 객체가 공유
print("s1 학교:", s1.school_name)
print("s2 학교:", s2.school_name)

# 인스턴스 변수는 객체마다 다름
print("s1 이름:", s1.name)
print("s2 이름:", s2.name)

# 클래스 변수를 변경하면 → 모든 객체에 영향
Student.school_name = "파이썬고등학교"
print("s1 학교:", s1.school_name)
print("s2 학교:", s2.school_name)
