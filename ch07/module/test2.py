# 모듈 불러오기
import mod2
mod2.hello()
mod2.hi()

# 모듈에서 특정함수만 불러오기
from mod2 import hello, hi
hello() # 모듈없이 함수만 사용 가능
hi()