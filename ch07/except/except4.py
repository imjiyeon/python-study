# 여러 개의 오류 처리하기

# try:
#     a = [1, 2]
#     print(a[3])
#     4 / 0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱할 수 없습니다.")

# 오류 변수 추가하고 에러메시지 확인
# try:
#     a = [1, 2]
#     print(a[3])
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)

# ZeroDivisionError와 IndexError를 함께 처리
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)
