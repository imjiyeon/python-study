# 응용

# **kwargs를 사용하여 학생 이름과 점수를 입력받는 calc 함수를 작성하세요
# 입력받은 학생들의 평균 점수를 출력하세요

def calc(**kwargs):
    # 여기에 코드를 작성하세요
    pass

calc(kim=90, lee=80, park=100)
# 평균: 90.0

def calc(**kwargs):
    total = sum(kwargs.values())     # 점수 합계
    avg = total / len(kwargs)        # 평균
    print("평균:", avg)

calc(kim=90, lee=80, park=100)
# 평균: 90.0
