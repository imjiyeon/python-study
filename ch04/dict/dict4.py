# import : 모듈을 불러오는 것
# 모듈 : 특정 기능을 미리 만들어둔 파이썬 파일
import copy

# 얇은 복사와 깊은 복사의 차이

# 객체 복사하기 (얇은 복사)
dic = {'name': '둘리', 'age': 10}
dic_copy = dic.copy()

# 복사본을 수정하면 원본은 영향 없음
dic_copy['age'] = 20
print("원본:", dic)
print("복사본:", dic_copy)

# 복잡한 객체 복사하기
dic = {'name': '둘리', 'age': 10, 'hobby': ['축구','야구']}
dic_copy = dic.copy()

# 복사복을 수정하면 원본도 함께 수정됨
# 이유는 hobby는 리스트이고, 리스트의 값이 아니라 주소가 복사됨
# 따라서 원본의 hobby와 복사본의 hobby가 같은 리스트를 바라보게됨
dic_copy['hobby'][0] = '테니스'
print("원본:", dic)
print("복사본:", dic_copy)

# 객체를 완벽하게 복사하기 위해 deepcopy 함수를 사용
dic = {'name': '둘리', 'age': 10, 'hobby': ['축구','야구']}
dic_deep = copy.deepcopy(dic)

dic_deep['hobby'][0] = '테니스'
print("원본:", dic) 
print("복사본:", dic_deep)