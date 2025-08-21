#문자열 교체 함수: replace

#첫번째인자: 교체대상
#두번째인자: 새로운문자

#replace 함수를 사용하여 -하이픈 제거
print("010-1234-5678".replace("-", ""))
print("+8210-1234-5678".replace("-", ""))
print("+82 10-1234-5678".replace("-", "").replace(" ", ""))


#문자열 공백제거 함수들

#양옆 공백 제거
print(repr("   Sun is shining.   ".strip()))
#왼쪽 공백 제거
print(repr("   Sun is shining.   ".lstrip()))
#오른쪽 공백 제거
print(repr("   Sun is shining.   ".rstrip()))
