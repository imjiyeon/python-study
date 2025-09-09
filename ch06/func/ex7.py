# 매개변수 초깃값 설정하기
def say_myself(name, age, gender='f'):
    print(f"나의 이름은 {name}입니다.")
    print(f"나이는 {age}살입니다.")
    if gender == 'm':
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("둘리", 27) # 입력값이 없으면 초기값을 사용함
say_myself("둘리", 27, 'm')
say_myself("둘리", 27, 'f')

# 초깃값 위치 오류 예제
# 초기값이 있는 매개변수는 항상 뒤쪽에 놓아야 한다!
# def say_myself(name, man=True, age):
#     print(f"나의 이름은 {name}입니다.")
#     print(f"나이는 {age}살입니다.")
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# say_myself("둘리", 27)