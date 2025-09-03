# 딕셔너리 관련 함수

dic = {'name': '둘리', 'phone': '010-1234-5678', 'birth': '0222'}

# 모든 키를 담은 dict_keys 객체를 반환
keys = dic.keys()
# dict_keys 객체는 리스트와 비슷하게 생겼지만 리스트는 아님
print(keys, type(keys))

# 필요하면 리스트로 변환해서 사용
lis = list(keys)
print(lis, type(lis))

# 모든 값을 담은 dict_values 객체 반환 
values = dic.values()
print(values)

# (key, value) 쌍을 담은 dict_items 객체 반환
items = dic.items()
print(items)

# key로 value 꺼내기
dic = {'name': '둘리', 'phone': '010-1234-5678', 'birth': '0222'}
print(dic.get('name'))
print(dic['phone'])

# 해당 key가 딕셔너리 안에 있는지 조사하기
print('name' in dic)
print('email' in dic)