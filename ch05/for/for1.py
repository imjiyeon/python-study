# 문자 리스트 생성
lis = ["a", "b", "c", "d", "e"]

# for 변수 in 자료구조
# for 변수 리스트
for ch in lis:
    print(ch)

# 딕셔너리 생성
dic = {"apple": 1200, "banana": 800, "orange": 1500}

# key만 출력
for k in dic:
    print(k)

# value만 출력
for v in dic.values():
    print(v)    

# key와 value 함께 출력
for k, v in dic.items():
    print(k, v)
