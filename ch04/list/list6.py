# iterable(이터러블) : 하나씩 차례대로 꺼낼 수 있는 객체
# 예: 문자열, 리스트, 튜플, 딕셔너리, set, range객체

# 리스트 이터레이터
it = iter([1, 2, 3])
for v in it:
    print(v)

# 문자열 이터레이터
it_str = iter("hello")
for ch in it_str:
    print(ch)