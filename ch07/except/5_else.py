# try-except-else 구조
# - 오류가 발생하면 except 실행
# - 오류가 발생하지 않으면 else 실행

try:
    age = int(input("나이를 입력하세요: "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age < 18:
        print("미성년자는 출입금지입니다.")
    else:
        print("환영합니다.")