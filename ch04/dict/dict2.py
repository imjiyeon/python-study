# 학생 딕셔너리 생성
students = {1: "둘리", 2: "도우너", 3: "또치"}

# 딕셔너리 쌍 추가
students[4] = '고길동'

# 딕셔너리 요소 삭제
del students[1]

# 딕셔너리에서 key를 사용해 value 꺼내기
print(students[2])

# 모든 값 출력하기
for key in students:
    print(students[key])
