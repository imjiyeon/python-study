# for문으로 새로운 리스트 만들기
nums = [1, 2, 3, 4]
new_nums = []
for n in nums:
    new_nums.append(n * 3)
print(new_nums)   # [3, 6, 9, 12]

# 리스트 컴프리헨션을 사용해 새로운 리스트 만들기
# [표현식 for 요소 in 자료구조]
nums = [1, 2, 3, 4]
new_nums = [n * 3 for n in nums]
print(new_nums)

# 리스트 컴프리헨션에서 조건문 추가
nums = [1, 2, 3, 4]
# 짝수만 고르기
result = [n * 3 for n in nums if n % 2 == 0]
print(result)   # [6, 12]
