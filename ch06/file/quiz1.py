# test.txt 파일을 만들고
# "hello"와 "hi"를 쓰세요
f = open("test.txt", 'w')
f.write("hello\n")
f.write("hi\n")
f.close()

# score.txt 파일을 만들고
# "80 90 70 100 60"를 쓰세요
f = open("score.txt", 'w')
f.write("80 90 70 100 60")
f.close()

# numbers.txt 파일을 만들고 10부터 20까지 쓰세요
f = open("numbers.txt", 'w')
for i in range(10, 21):          
    f.write(f'{i}\n')

f.close()
