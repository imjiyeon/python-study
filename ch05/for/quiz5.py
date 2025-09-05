# 리스트에서 가장 큰 값을 구하세요
nums = [5, 9, 3, 8, 2]

max = nums[0]

for n in nums:
    if n > max:
        max_val = n
print("최댓값:", max_val)

# 과정
# 5 9 비교 => 9 (max nums[1])
# 9 3 비교 => 9 (max nums[2])
# 9 8 비교 => 9 (max nums[3])
# 9 2 비교 => 9 (max nums[4])
# 현재 가장큰값, 리스트의 요소