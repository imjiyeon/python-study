# 날짜와 시간

# datetime 모듈 불러오기
from datetime import datetime, date, time

# 날짜와 시간 생성
dt = datetime(2025, 9, 11, 20, 30, 0)

# 날짜와 시간 속성 접근
print(dt.day)       # 11
print(dt.minute)    # 30

# 날짜와 시간으로 분리
print(dt.date())    # 2025-09-11
print(dt.time())    # 20:30

# datetime -> 문자열로 변환
print(dt.strftime("%Y-%m-%d %H:%M")) # '2025-09-11 20:30'

# 문자열 -> datetime 객체로 변환
print(datetime.strptime("20250910", "%Y%m%d"))
