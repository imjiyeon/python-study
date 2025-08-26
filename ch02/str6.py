#문자열 교체 함수: replace

#첫번째인자: 교체대상
#두번째인자: 새로운문자

# replace 함수를 사용하여 문자 변경
print("banana".replace("a", "o"))

#replace 함수를 사용하여 -하이픈 제거
print("010-1234-5678".replace("-", ""))

#양쪽에 작은따음표 표시: repr
print(repr("   Hello World   "))

#문자열 공백제거 함수들

#양옆 공백 제거
print(repr("   Hello World   ".strip()))
#왼쪽 공백 제거
print(repr("   Hello World   ".lstrip()))
#오른쪽 공백 제거
print(repr("   Hello World   ".rstrip()))

# title: 첫글자를 대문자로 바꾸는 함수
text = "hello world from python"
print(text.title())