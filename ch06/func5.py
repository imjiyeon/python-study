# 키워드 매개변수 **kwargs
# 전달받은 인자를 모아 딕셔너리를 만든다
# 인자는 반드시 쌍으로 전달해야 한다

# 함수에서 매개변수의 개수를 유연하게 받고 싶을 때 사용한다
# kwargs를 사용하면 매개변수를 여러개 받을 수 있다

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)