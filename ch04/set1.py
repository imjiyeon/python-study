# 집합(set) 만들기
s1 = {1,2,3}

# 빈 set
s2 = set()
print(s2, type(s2))

# 빈 set은 중괄호로 만들면 안됨. 딕셔너리로 인식됨
s2 = {}
print(s2, type(s2))

# list -> set
s3 = set([1, 2, 3])
print(s3)

# string -> set
s4 = set("Hello")

# 그런데 결과를 보면 l이 하나밖에 없다
# set은 중복을 허용하지 않기 때문에 같은 값은 하나만 저장된다
# set은 순서가 없기 때문에 추가한 순서대로 나오지 않는다
print(s4)  # {'e', 'H', 'l', 'o'}