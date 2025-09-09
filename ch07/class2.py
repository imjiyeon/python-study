# 학생 클래스 만들기

class Student:
    def setdata(self, id, name, grade):
        self.student_id = id   # 학번
        self.name = name       # 이름
        self.grade = grade     # 학년

    def info(self):
        print(f"저는 {self.grade}학년 {self.name}입니다.")


# 클래스 사용하기
student1 = Student()
student1.setdata(101, '둘리', 2)
student1.info()

student2 = Student()
student2.setdata(102, '도우너', 2)
student2.info()

# student3 = Student()
# student3.info()