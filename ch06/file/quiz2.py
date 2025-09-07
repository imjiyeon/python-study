# test.txt 파일을 읽고 출력하세요
# f = open("test.txt", 'r')
# data = f.read()
# print(data)
# f.close()

# score.txt 파일을 읽고 합계와 평균을 구하세요
f = open("score.txt", 'r')
data = f.read()
scores = data.split()

total = 0
for s in scores:
    total += int(s)

average = total / len(scores)

print("합계:", total)
print("평균:", average)
f.close()

# numbers.txt 파일을 읽고 짝수만 출력하세요
# f = open("numbers.txt", 'r')
# lines = f.readlines()

# for line in lines:
#     if int(line) % 2 == 0:
#         print(line, end='')

# f.close()
