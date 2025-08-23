# return의 다른 쓰임새
# 특정 조건에서 함수를 중간에 빠져나가고 싶을때 사용한다
# 리턴값 없이 return 키워드를 사용하면 함수가 종료된다

def say_nick(nick):
    if nick == "바보":
        return
    print(f"나의 별명은 {nick}입니다.")

say_nick("야호")
say_nick("바보")