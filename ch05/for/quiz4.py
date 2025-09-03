# 리스트에서 가장 큰 값을 구하세요
nums = [5, 9, 3, 8, 2]

max = nums[0]

for n in nums:
    if n > max:
        max_val = n
print("최댓값:", max_val)
