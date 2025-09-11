# raise : 오류를 일부러 발생시키는 명령어

# class Bird:
#     def fly(self):
#         raise NotImplementedError
    
# class Eagle(Bird):
#     pass

# eagle = Eagle()
# eagle.fly()

# 오류를 해결하기 위해 반드시 fly 함수를 구현해야 한다
# 자식 클래스에서 함수를 재정의하는 것을 유도할때 사용한다
class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird):
    def fly(self):
        print("very fast")  

eagle = Eagle()
eagle.fly()
