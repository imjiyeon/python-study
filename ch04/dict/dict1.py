# 딕셔너리 생성
dic = {'name': '둘리', 'phone': '010-1234-5678', 'birth': '0222'}

# 딕셔너리 쌍 추가
# dic[key] = value
dic['age'] = 20
dic['address'] = '인천'

# 딕셔너리 요소 삭제
# del dic[key]
del dic['name']

# 딕셔너리에서 key를 사용해 value 꺼내기
print(dic['phone'])


# 학생 딕셔너리 생성
students = {1: "둘리", 2: "도우너", 3: "또치"}

# 딕셔너리 쌍 추가
students[4] = '고길동'

# 딕셔너리 요소 삭제
del students[1]

# 딕셔너리에서 key를 사용해 value 꺼내기
print(students[2])
