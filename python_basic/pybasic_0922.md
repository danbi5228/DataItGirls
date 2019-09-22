# Python Basic class 2

## 되돌아보기

* None 은 is 로 비교하자!
```python
a == None
a is None
```

둘 다 돌아갈 때도 있지만 == 은 상황에 따라 돌아가지 않을 때가 있다.
따라서 None은 is 와 함께 비교하자!

* == : 값 비교
  is : 주소값도 비교. 값이 같은데 주소값이 다르면 False를 return

* 비트연산
특히 쉬프트 연산 (>>, <<) 을 쓰게되면 속도가 굉장히 빠르다.
속도가 중요한 프로그램의 경우, 쉬프트 연산은 하드웨어가 할 수 있는 가장 간단하고 빠른 연산이므로 쉬프트 연산을 주로 사용한다.

* 매개변수 : 입력값을 표현하는 변수로써 함수 내에서 해당 변수명으로 사용된다.
  전달인자 : 함수에게 전달해주는 인자
    ```python
    def hello(name) ~ # name - 매개변수
    hello ('Leila')   # Leila - 전달인자
    ```


## String

* replace : 찾아서 바꾸려는 것이 글자수가 서로 달라도 치환 가능!
```python
a = 'hello world'
a = a.replace('world', 'hi')
print(a) # 'hello hi'
```

* split
strip() : string 내장함수. 문자열 양쪽의 공백 지우기 (list type에서는 쓸 수 없다!)
lstrip() / rstrip() : 왼쪽 공백 제거 / 오른쪽 공백 제거

ex 1)
```python
b = ['Apple ', ' banana ', ' melon']
이 때 각각의 element들의 공백을 제거하고 싶을 때 그냥 .strip 은 동작하지 않으므로
c = [c.strip() for c in b] # 각각의 공백이 제거된 list를 저장할 수 있다!!
print(c) 
```
ex 2)
```python
a = 3
b = "Bigger than 5" if a > 5 else "smaller than 5"
print(b) # smaller than 5
```

* 대/소문자 바꾸기 = upper() / lower()

* 문자열 포맷팅 (String formatting)
round((5/3), 2) # 나눈 값의 소숫점 2번째 자리까지 return

```python
# Old
print("%s and %d" % ("Apple", 10))

# New
print("{} and {}" )

# 소수점 둘째자리까지 표현
print("{:.2f}".format(4/3)) # 1.33
# 무조건 4자리로 표현
print("{:04d}".format(12)) # 0012

print("{:x4d}".format(12)) # 오류
print("{: 4d}".format(12)) # 공백+숫자 (총 4자리가 되게끔)
# +와 -는 부호의 의미로서 사용 가능
```


## Collection

## List
* sort : sort() - 오름차순 정렬, sort(reverse = True) - 내림차순 정렬
* stack : pop() - 마지막에 append한 값을 return
* queue
: print는 queue의 구조. list와 stack을 이용해서도 구현은 가능하나 느리게 동작.
 ```python
  from collections import deque
  queue = deque([1, 2, 3])
  queue.popleft()
```

## Tuple
* 리스트와 매우 비슷하나, 수정이 불가능하다. 따라서 특정 index에 값을 '새로 할당'하는 것이 불가능하다. (인덱스로 '접근'만 가능하다.)
그래서 함수에서 여러개의 리턴값을 가질 때, 튜플 형태로 표현된다.

## Dictionary
* Key-value 쌍으로 이루어진 데이터타입
* 인덱스가 아닌 Key 를 통해 Value에 접근이 가능하다.
* 직접 딕셔너리를 생성해도 되고 constructor 를 이용하여 생성도 가능하다.
```python
# 둘다 똑같다!!
tel = {'a': 1, 'b': 2}
tel = dict(a=1, b=2)
```
* key값은 unique해야하지만 만약 똑같은 key 값을 넣으면, 맨 마지막 것 외에는 모두 무시된다.
* list처럼 for 문을 사용할 수 있다.
* 'Leila' in tel 과 같은 문장으로 있다/없다를 True/False로 받아낼 수 있다.
* get() : 
```python
    tel.get('leila') # 'leila' key가 있으면 value return. 없으면 None. 아무것도 출력하지 않는다. 
    tel.get('leila', 'N/A') # key leila가 있으면 그 value를 가져오고, 아니면 'N/A' 를 return
```

## Set
* 집합의 형태를 쉽게 처리하기 위한 데이터 타입. 딕셔너리와 비슷하지만 key가 없는 형태이다.
* 중복을 허용하지 않는다.
* 교집합, 합칩합, 차집합 구하기
``` python
    a & b # 교집합. 둘다 만족해야 하므로
    a | b # 합집합. 둘중 하나라도 만족하면 되므로 합치는 것
    a - b # 차집합
    b - a # 차집합
```
