# return의 다른 쓰임새
# 특정 조건에서 함수를 중간에 빠져나가고 싶을때 사용한다
# 리턴값 없이 return 키워드를 사용하면 함수가 종료된다

def say_nick(nick):
    if nick == "바보":
        return
    print(f"나의 별명은 {nick}입니다.")

say_nick("야호")
say_nick("바보")


# 파이썬 함수는 사실 하나의 값만 반환 가능하다
# return에 여러 개를 쓰면 자동으로 '튜플'로 묶어서 반환한다
def f():
    a = 5
    b = 6
    c = 7
    return a, b, c   # 튜플 반환

t = f()
print(t) 