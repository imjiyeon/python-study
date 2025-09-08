# 아래 코드에서 각 변수에 무엇이 저장되는지 주석을 작성하세요

# 리스트를 입력받아 첫 번째 값을 반환하는 함수 만들기
def func(lis): # lis : ?
    return lis[0]

my_lis = [10, 20, 30] # my_lis : ?
result = func(my_lis) # result : ?
print(result)

def func(lis):   # lis : 함수 매개변수로, 함수 내부에서 선언됨
    return lis[0]

my_lis = [10, 20, 30]   # my_lis : 함수에 전달하기 위한 리스트로, 
result = func(my_lis)   # result : my_lis의 첫 번째 값인 10이 저장됨
print(result)           # 출력 결과 : 10


# 아래 코드에서 각 변수에 무엇이 저장되는지 주석을 작성하세요

# 문자열을 입력받아 길이를 반환하는 함수 만들기
def func(msg): # msg : ?
    return len(msg)

my_str1 = "abc" # my_str1 : ?
result1 = func(my_str1) # result1 : ?
my_str2 = "hello" # my_str2 : ?
result2 = func(my_str1) # result2 : ?
