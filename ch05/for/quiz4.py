# 변수n을 선언하고 숫자를 대입하세요
# n의 크기만큼 *별을 출력하세요
# n=5 -> *****

n = 5
str = ''
for i in range(n):
    str = str+'*'
print(str)    

# 변수n을 선언하고 숫자를 대입하세요
# n의 크기만큼 삼각형을 그려주세요
# n=3
# =>
# *
# **
# ***
n = 3
for i in range(1,n+1):
    print('*' * i)

# 변수n을 선언하고 숫자를 대입하세요
# n의 크기만큼 삼각형을 그려주세요
# n=5
# =>
#     *
#    **
#   ***
#  ****
# *****
n = 3
for i in range(1,n+1):
    print('*' * i)




# 구구단 3단을 출력하세요
for i in range(1, 10):
    print(f"3 x {i} = {3*i}")

