#if문
#조건은 날씨 (맑음 또는 비)
weather = "맑음"
print("비가 내리는가?", weather == "비")

#조건을 만족하면 if문이 실행됨
if weather == "비":
    print("우산을 가져간다")

#if~else
#조건을 만족하면 if문 실행되고, 그렇지않으면 else문이 실행됨
if weather == "비":
    print("우산을 가져간다")
else:
    print("우산을 가져가지 않는다")

#if~elif~else
#새로운 조건은 elif로 추가
if weather == "비":
    print("우산을 가져간다")
elif weather == "눈":
    print("장화를 신고 나간다")
else:
    print("그냥 나간다")