# 다음과 같이 학생 점수 딕셔너리를 만들어주세요
scores = {"철수": 80, "영희": 95, "민수": 70, "지연": 100}

# for문을 사용해 전체 평균 점수를 구하세요
total = 0
count = 0
for name in scores:
    total += scores[name]
    count += 1
print("평균 점수:", total / count)

# 90점 이상 학생의 수를 구하세요.
cnt = 0
for name in scores:
    if scores[name] >= 90:
        cnt += 1
print("90점 이상 학생 수:", cnt)
