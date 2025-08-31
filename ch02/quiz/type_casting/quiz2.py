# 다음 코드를 보고 예상 결과를 미리 작성하세요

d = 1.2
f = 0.9

i = int(d)           # ?
i2 = int(f)          # ?
i3 = int(d) + int(f) # ?
i4 = int(d + f)      # ?

# # 결과
# i = int(d)           # 1.2 → 1
# i2 = int(f)          # 0.9 → 0
# i3 = int(d) + int(f) # 1 + 0 → 1
# i4 = int(d + f)      # (1.2 + 0.9) = 2.1 → 2

# # int로 형변환을 하면 소수점 이하는 버린다
# print(i)   # 1
# print(i2)  # 0
# print(i3)  # 1
# print(i4)  # 2
