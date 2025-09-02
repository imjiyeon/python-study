# 1번 문제
shopping = ["우유", "빵", "달걀"]

# 1) "사과" 추가
shopping.append("사과")
# 2) 두 번째 요소(빵)를 "치즈"로 수정
shopping[1] = "치즈"
# 3) "우유" 삭제
shopping.remove("우유")

print("결과:", shopping)   # ['치즈', '달걀', '사과']


# 2번 문제
scores = [60, 75, 80, 90]

# 1) 100 추가
scores.append(100)
# 2) 세 번째 요소(80)를 85로 수정
scores[2] = 85
# 3) 마지막 요소 꺼내면서 삭제
last = scores.pop()

print("결과:", scores, "꺼낸 값:", last)   # [60, 75, 85, 90] 꺼낸 값: 100


# 3번 문제
animals = ["강아지", "고양이", "토끼", "햄스터"]

# 1) "고양이"를 "고슴도치"로 수정
animals[1] = "고슴도치"
# 2) 첫 번째 요소 삭제
del animals[0]
# 3) 마지막 요소 꺼내면서 삭제
last_animal = animals.pop()

print("결과:", animals, "꺼낸 값:", last_animal)   # ['고슴도치', '토끼'] 꺼낸 값: 햄스터
