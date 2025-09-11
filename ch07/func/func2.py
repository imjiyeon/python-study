# sorted : 정렬 (리스트로 반환)
print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))
print(sorted("zero"))

# reversed : 역정렬
print(list(reversed([1, 2, 3, 4])))  

# sum : 합계
print(sum([1, 2, 3]))

# type : 자료형 확인
print(type("abc"))

# abs : 절댓값
print(abs(-3))
print(abs(-1.2))

# enumerate : 인덱스 붙이기
print(enumerate(['body', 'foo', 'bar']))
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name) # 인덱스, 값

# zip : 리스트나 튜플을 하나로 묶기
# 위치를 기반으로 값을 묶어줌
seq1 = ["foo", "bar", "baz"]
seq2 = ["one", "two", "three"]
print(zip(seq1, seq2)) # zip 객체 반환
print(list(zip(seq1, seq2))) # 쌍으로 묶인 리스트 반환
