# 기본 문법

# 나머지 매개변수를 사용하여 입력받은 과일의 이름만 출력하세요
# 결과) apple, banana, orange

def calc(**kwargs):
    # 여기에 코드를 작성하세요
    pass

calc(apple=1200, banana=800, orange=1500)

# 정답
def calc(**kwargs):
    for key in kwargs:          
        print(key)

calc(apple=1200, banana=800, orange=1500)

# 나머지 매개변수를 사용하여 입력받은 학생의 점수만 출력하세요
# 결과) 90, 85, 100

def show_scores(**kwargs):
    # 여기에 코드를 작성하세요
    pass

show_scores(철수=90, 영희=85, 민수=100)

# 도시 이름과 인구 수를 모두 출력하세요 (인구 수는 만 명 단위)
# 결과) seoul 950, busan 340, incheon 300

def show_population(**kwargs):
    # 여기에 코드를 작성하세요
    pass

show_population(seoul=950, busan=340, incheon=300)

# 나머지 매개변수를 사용하여 입력받은 상품의 상품명만 출력하세요
# 결과) milk bread egg (가격은 무시하고 상품명만 출력)

def show_items(**kwargs):
    # 여기에 코드를 작성하세요
    pass

show_items(milk=2500, bread=2000, egg=3000)