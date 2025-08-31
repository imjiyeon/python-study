# 문자열 "AI" 에서 인덱싱을 이용해 "A" 와 "I" 를 각각 출력하세요
text = "AI"
print(text[0])    # A
print(text[1])    # I

# 문자열 "Korea" 에서 인덱싱을 이용해 "K" 와 "a" 를 각각 출력하세요
word = "Korea"
print(word[0])   # K
print(word[4])   # a

# 문자열 lang = "Programming" 의 마지막 글자를 출력하세요
lang = "Programming"         
last = len(lang) # 11
print(lang[last-1])  # g

# 문자열 "Python" 에서 슬라이싱을 이용해 "Py" 와 "thon" 을 각각 출력하세요
word = "Python"
print(word[:2])   # Py
print(word[2:])   # thon
