# 인덱싱
t1 = (1, 2, 'a', 'b')
print (t1)
print (t1[0], t1[3])

# 슬라이싱
t1 = (1, 2, 'a', 'b')
print(t1[1:])

# 튜플 연결하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
print(t3)

# 튜플 곱하기
t2 = (3, 4)
t4 = t2 * 3
print(t4)

# 튜플 길이 구하기
t1 = (1, 2, 'a', 'b')
length = len(t1)
print(length)

# 리스트에 포함된 특정요소의 개수 세기
t5 = (1,2,2,2,3,4,2)
print(t5.count(2))