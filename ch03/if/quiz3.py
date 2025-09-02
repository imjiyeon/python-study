# 변수를 선언하고 'b', 'c', 'd' 중 하나를 입력하세요
# 문자에 해당하는 동물을 출력하세요
# 조건에 맞는 동물이 없으면 "none"을 출력하세요
#
# b - 새
# c - 고양이
# d - 강아지

animal = 'b'  # b, c, d

if animal == 'b':
    print("bird")
elif animal == 'c':
    print("cat")
elif animal == 'd':
    print("dog")
else:
    print("none")


time = 10

if time < 9:
    print("출근 준비")
elif time < 12:
    print("오전 업무")
elif time < 13:
    print("점심 식사")
elif time < 18:
    print("오후 업무")
elif time < 21:
    print("야근 중")
else:
    print("퇴근 후 휴식")
