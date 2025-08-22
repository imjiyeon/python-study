# 딕셔너리 관련 함수

dic = {'name': '둘리', 'phone': '010-1234-5678', 'birth': '0222'}

# key 리스트 만들기
keys = dic.keys()

# dict_keys 객체 리턴
# dict_keys 객체는 리스트와 달리 append, insert, remove, sort 함수를 사용할 수 없다
print(keys, type(keys))

# 객체 -> 리스트 변환
list = list(keys)
print(list, type(list))

# value 리스트 만들기
values = dic.values()

# dict_values 객체 리턴
print(values, type(values))

# key,value 쌍 리스트 만들기
items = dic.items()
print(items, type(items))

# 딕셔너리의 모든 요소 지우기
dic.clear()
print(dic)

# key로 value 꺼내기
dic = {'name': '둘리', 'phone': '010-1234-5678', 'birth': '0222'}
print(dic.get('name'))
print(dic.get('phone'))
print(dic['birth'])

# 해당 key가 딕셔너리 안에 있는지 조사하기
print('name' in dic)
print('email' in dic)