# range()는 연속된 숫자를 만들어주는 함수로, for문 함께 자주 사용된다
# 0부터 9까지의 숫자 10개가 반환됨
# range(개수)
nums = range(10)
print(nums)

# "안녕하세요" 10번 출력
for n in nums:
    print("안녕하세요")

# 1부터 10까지 숫자 10개가 반환됨
# range(시작숫자,끝숫자) 마지막숫자는 포함안됨
nums = range(1,11)
print(nums)

# 1부터 10까지 하나씩 출력
for n in nums:
    print(n)
