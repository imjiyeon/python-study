# 다음 코드를 보고 예상되는 실행 결과를 작성하세요

temp = ('bird', 'cat', 'dog')
b, c, d = temp
print(b, c, d) # ?

# 정답
# 'bird', 'cat', 'dog'


fruits = ("사과", "배", "포도", "귤", "딸기")

# 1)첫 번째 과일만 a에 넣고, 나머지는 rest에 담으세요
a, *rest = fruits
print(a) 
print(rest)

# 2)앞 2개만 x, y에 넣고, 나머지는 others에 담으세요
x, y, *others = fruits
print(x, y) 
print(others)
