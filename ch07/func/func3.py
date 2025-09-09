# 날짜와 시간

# datetime 모듈 불러오기
from datetime import datetime, date, time

# 특정 날짜와 시간 생성
dt = datetime(2011, 10, 29, 20, 30, 21)

# 날짜와 시간 속성 접근
print(dt.day)       # 29
print(dt.minute)    # 30

# date()와 time() 메서드로 분리
print(dt.date())    # datetime.date(2011, 10, 29)
print(dt.time())    # datetime.time(20, 30, 21)

# 문자열로 변환 (strftime)
print(dt.strftime("%Y-%m-%d %H:%M"))  
# '2011-10-29 20:30'

# 문자열을 datetime 객체로 변환 (strptime)
print(datetime.strptime("20091031", "%Y%m%d"))  
# datetime.datetime(2009, 10, 31, 0, 0)

# replace로 특정 필드 교체
dt_hour = dt.replace(minute=0, second=0)
print(dt_hour)  
# datetime.datetime(2011, 10, 29, 20, 0)

# datetime 간의 차이 (timedelta)
dt2 = datetime(2011, 11, 15, 22, 30)
delta = dt2 - dt
print(delta)        # datetime.timedelta(days=17, seconds=7179)
print(type(delta))  # datetime.timedelta

# timedelta를 더하거나 빼기
print(dt + delta)   # datetime.datetime(2011, 11, 15, 22, 30)
