#문자열 인덱싱
#문자열[인덱스]
#인덱스번호: 0부터시작 ~ 문자열길이-1
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])

#문자열 자르기
#문자열[시작위치:끝위치]
print("KE901"[0:2])
print("KE901"[2:5])
print("KE901"[2:])
print("KE901"[:2])
print("KE901"[:])

print("010-1234-5678"[:3])
print("010-1234-5678"[4:8])
print("010-1234-5678"[9:])

#문자열 길이를 구하는 함수: len
print(len("AAA"))
print(len("Hello, World"))
print(len("안녕하세요"))
