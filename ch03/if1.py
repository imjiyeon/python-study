# 조건문

# if문
# 조건은 나이
age = 10
print("나이가 8살 이상인가?", age >= 8)

# 조건을 만족하면 if문이 실행됨
if age >= 8:
    print("학교에 다닙니다")

# if ~ else
# 조건을 만족하면 if문 실행되고, 그렇지 않으면 else문이 실행됨
if age >= 8:
    print("학교에 다닙니다")
else:
    print("학교에 다니지 않습니다")

# if ~ elif ~ else
# 새로운 조건은 elif로 추가
if age < 8:
    print("아동입니다")
elif age < 14:
    print("초등학생입니다")
elif age < 20:
    print("중,고등학생입니다")
else:
    print("성인입니다")
