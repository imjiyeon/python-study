# 집합(set) 만들기
s1 = {1,2,3}

# 중괄호{}는 빈 set이 아니고 빈 딕셔너리가됨
s2 = {}
print(s2, type(s2))

# 빈 set
s2 = set()
print(s2, type(s2))

# list -> set
s3 = set([1, 2, 3])
print(s3)

# string -> set
s4 = set("Hello")

# 문자열을 set으로 바꾸면 중복 문자는 하나만 남고, 순서도 유지되지 않는다
print(s4)  # {'e', 'H', 'l', 'o'}