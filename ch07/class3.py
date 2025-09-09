# 생성자

class Student:
    # __init__ : 객체가 생성될 때 자동으로 호출되는 생성자
    def __init__(self, student_id, name, grade):
        self.student_id = student_id   # 학번
        self.name = name               # 이름
        self.grade = grade             # 학년

    def info(self):
        print(f"저는 {self.grade}학년 {self.name}입니다.")

    def study(self):
        print("공부를 합니다.")    


# 에러남
# student = Student()        

# 첫번째 학생 만들기
student1 = Student(101, "둘리", 2)
print("학번:", student1.student_id)
print("이름:", student1.name)
print("학년:", student1.grade)
student1.info()

# 두번째 학생 만들기
student2 = Student(102, "도우너", 2)
print("학번:", student2.student_id)
print("이름:", student2.name)
print("학년:", student2.grade)
student2.info()