# 1.
# math 모듈을 가져와서 ceil(실수) 함수로 올림하여 출력하세요
# 예) 3.14 → 4
# math 모듈을 가져와서 floor(실수) 함수로 내림하여 출력하세요
# 예) 3.14 → 3
import math

print(math.ceil(3.14))   # 올림
print(math.floor(3.14))  # 내림

# 2.
# random 모듈을 가져와서 randint(시작, 끝) 함수로
# 1~6 사이의 랜덤 숫자 6개를 뽑아보세요

import random

for i in range(6):
    print(random.randint(1, 6))

# 3.
# time 모듈을 가져와서 sleep(초) 함수로
# 2초 동안 기다린 뒤 "끝!"을 출력하세요

import time

time.sleep(2)
print("끝!")

# 4.
# os 모듈을 가져와서 getcwd() 함수로
# 현재 작업 경로를 출력하세요

import os

print("현재 경로:", os.getcwd())