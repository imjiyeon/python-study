# 조건문 만들기

# if : 조건이 참이면 실행하는 문법
age = 10

# 나이가 8살이상이면 실행됨
if age >= 8:
    print("학교에 다닙니다")

# if ~ else : 조건이 참이면 if문이 실행되고, 거짓이면 else문이 실행됨
if age >= 8:
    print("학교에 다닙니다")
else:
    print("학교에 다니지 않습니다")

# if ~ elif ~ else : 여러 조건을 순서대로 검사
if age < 8:
    print("아동입니다")
elif age < 14:
    print("초등학생입니다")
elif age < 20:
    print("중,고등학생입니다")
else:
    print("성인입니다")
