# 나머지 매개변수로 입력받는 calc 함수를 작성하세요
# **kwargs를 사용하여 입력받은 과일의 이름만 출력하세요

def calc(**kwargs):
    # 여기에 코드를 작성하세요
    pass

calc(apple=1200, banana=800, orange=1500)
# apple
# banana
# orange

# 정답
def calc(**kwargs):
    for key in kwargs:          
        print(key)

calc(apple=1200, banana=800, orange=1500)


# 나머지 매개변수로 입력받는 introduce 함수를 작성하세요
# **kwargs를 사용하여 입력받은 사람의 정보를 모두 출력하세요

def introduce(**kwargs):
    # 여기에 코드를 작성하세요
    pass

# 실행 예시
introduce(name="둘리", age=10, city="서울")
# name: 둘리
# age: 10
# city: 서울

# 정답
def introduce(**kwargs):
    for key, value in kwargs.items():          
        print(key,':',value)
        
introduce(name="둘리", age=10, city="서울")

