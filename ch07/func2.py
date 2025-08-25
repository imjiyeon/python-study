# sorted : 정렬 (리스트로 반환)
print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))
print(sorted("zero"))
print(sorted((3, 2, 1)))

# reversed : 역정렬
print(list(reversed([1, 2, 3, 4])))  

# sum : 합계
print(sum([1, 2, 3]))
print(sum((4, 5, 6)))

# type : 자료형 확인
print(type("abc"))

# abs : 절댓값
print(abs(3))
print(abs(-3))
print(abs(-1.2))

# enumerate : 인덱스 + 값
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)