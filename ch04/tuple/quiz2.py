nums = (10, 20, 30, 40, 50, 60)

# 인덱스 2번부터 4번까지 잘라서 출력하세요
print(nums[2:5])

# 처음부터 인덱스 3번 전까지 잘라서 출력하세요
print(nums[:3]) 

# 인덱스 2번부터 끝까지 잘라서 출력하세요
print(nums[2:])

fruits = ("사과", "배", "포도", "귤", "딸기")

# 첫 번째 과일만 a에 넣고, 나머지는 rest에 담으세요
a, *rest = fruits
print(a) 
print(rest)

# 앞 2개만 x, y에 넣고, 나머지는 others에 담으세요
x, y, *others = fruits
print(x, y) 
print(others)
