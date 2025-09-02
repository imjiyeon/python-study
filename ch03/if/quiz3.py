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


# 변수를 선언하고 시간을 입력하세요
# 시간에 따라 할일을 출력하세요
#
# 9시 - 출근
# 10시 - 회의
# 11시 - 서류 정리
# 12시 - 점심 식사
# 그외 시간 - 휴식

time = 10

if time == 9:
    print("출근")
elif time == 10:
    print("회의")
elif time == 11:
    print("서류 정리")
elif time < 12:
    print("점심 식사")
else:
    print("휴식")


# 변수를 선언하고 'b', 't', 'c' 중 하나를 입력하세요
# 문자에 해당하는 교통수단을 출력하세요
#
# b - 버스
# t - 지하철
# c - 자전거
transport = "t"

if transport == "b":
    print("버스")
elif transport == "t":
    print("지하철")
elif transport == "c":
    print("자전거")
else:
    print("도보")
