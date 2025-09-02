import copy

# 객체 복사하기 (얇은 복사)
dic = {'name': '둘리', 'age': 10}
dic_copy = dic.copy()

# 복사본만 수정되고, 원본은 수정 안됨
dic_copy['age'] = 20
print("원본:", dic)
print("복사본:", dic_copy)

# 복잡한 객체 복사하기
dic = {'name': '둘리', 'age': 10, 'hobby': ['축구','야구']}
dic_copy = dic.copy()

# 원본도 함께 수정됨
# hobby는 원본과 같은 리스트를 참조하기 때문
dic_copy['hobby'][0] = '테니스'
print("원본:", dic)
print("복사본:", dic_copy)

# 문제를 해결하기 위해서 깊은 복사로 완벽하게 복사하기
dic = {'name': '둘리', 'age': 10, 'hobby': ['축구','야구']}
dic_deep = copy.deepcopy(dic)

dic_deep['hobby'][0] = '테니스'
print("원본:", dic) 
print("복사본:", dic_deep)