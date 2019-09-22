# 두 수를 더하는 함수
def add(a, b):
    return a+b


# 두 수를 곱하는 함수
def mul(a, b):
    return a*b


# 두 수를 더한 값과 곱한 값을 같이 리턴하는 함수
def add_and_mul(a, b):
    #  def add_and mul(a, b = 0)  과 같이 디폴트값을 설정할 수 있다.
    #  디폴드 파라미터 뒤에 non-default 값이 올 수 없다.
    return add(a, b), mul(a, b)


print(add_and_mul(3, 5))
# print(add_and_mul(b=5, a=3)) # 가능!!!

# 따로따로 주는 것도 가능하다!!
# add_num, mul_num = add_and_mul(3, 5)
# print(add_num, mul_num)