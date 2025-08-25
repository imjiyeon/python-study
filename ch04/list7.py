# iterable(이터러블) : 하나씩 차례대로 꺼낼 수 있는 객체
# 문자열, 리스트, 튜플, 딕셔너리, set, range객체

# iterable: 대상이 iterable인지 확인하는 함수

# 문자열은 iterable 객체이므로 str_iterator가 반환됨
print(iter("a string"))

# 리스트는 iterable이므로 list_iterator가 반환됨
print(iter([1, 2, 3]))

# 정수는 iterable이 아니므로 에러남
# print(iter(5))
