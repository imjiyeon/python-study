# 리스트에 요소 추가/수정/삭제

lis = [1,2,3]

# 리스트에 새로운 요소 추가하기
lis.append(4)
print(lis)

lis.append(5)
print(lis)

# 특정 위치에 새로운 요소 추가하기
# insert 함수의 인자: 특정위치,새로운값
lis.insert(0, 4) # 0번째 자리에 4를 삽입
print(lis)

# 리스트의 값 수정하기
lis[2] = 4
print(lis) # lis[2]의 값을 변경

# 리스트 요소 삭제하기
# del 함수를 사용해 lis[1] 삭제
del lis[1] 
print(lis)

# 값으로 요소 삭제하기
# remove(value)
lis.remove(3)
print(lis)
# 리스트가 4를 여러개 가지고 있으면, 첫번째 4만 삭제된다
lis.remove(4)
print(lis)

# 마지막 요소 꺼내기
# pop은 리스트의 마지막 요소를 리턴하고 그요소는 삭제된다
last = lis.pop()
print(lis, last)

# 위치를 지정하면 해당 요소를 리턴하고 그요소는 삭제된다
last = lis.pop(1)
print(lis, last)
