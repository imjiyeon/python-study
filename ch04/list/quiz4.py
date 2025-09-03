# 빈 리스트 fruits를 만들고, 
# "사과", "바나나", "포도"를 차례대로 추가하세요
fruits = []
fruits.append("사과")
fruits.append("바나나")
fruits.append("포도")
print(fruits) # ['사과', '바나나', '포도']

# numbers 리스트의 두 번째 요소(20)를 99로 바꾸세요
numbers = [10, 20, 30, 40]
numbers[1] = 99
print(numbers) # [10, 99, 30, 40]

# animals 리스트에서 첫 번째 요소를 삭제하세요
animals = ["강아지", "고양이", "토끼"]
del animals[0]
print(animals) # ['고양이', '토끼']

# subjects 리스트에서 "영어"를 삭제하세요
subjects = ["국어", "영어", "수학", "과학"]
subjects.remove("영어")
print(subjects)   # ['국어', '수학', '과학']

# scores 리스트에서 마지막 요소를 꺼내면서 삭제하세요
scores = [70, 80, 90, 100]
last = scores.pop()
print(scores, last)   # [70, 80, 90] 100
