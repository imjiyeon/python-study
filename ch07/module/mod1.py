# 모듈 만들기

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# 테스트
# 테스트 코드 있으면, 모듈 import해도 5,6이 나옴
# __name__ : 파이썬 내부에서 사용하는 특별한 변수
# 실행하는 파일이 메인일때만 테스트코드가 실행됨
if __name__ == "__main__":
    print(add(1,4))
    print(add(4,2))