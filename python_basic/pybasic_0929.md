# Python Basic class 2

## 되돌아보기

* List Comprehension
```python
c = [c.strip().upper() for c in b]
```
-> 위의 코드를 일반적인 for loop 형태로 표현하면 
```python
tmp_list = []
for c in b:
    temp_list += [c.strip().upper()]
c = temp_list
```
tmp_list 를 따로 둬야 하는 것이 가장 큰 차이 ! 
바로 c에 넣으려는 것은 오류가 날 것이다!

-> 위의 코드를 함수 형태로 표현하면
```python
def strip_and_upper(string_list):
    """
    문자열 리스트안의 모든 원소들의 공백을 제거하고 대문자로 변환하는 함수
    """
     result = []
     for string in string_list:
             result += [string.strip().upper()]
     return result
```
주석 안의 내용은 내장함수 help()를 통해 나타나는 함수의 설명 부분이 된다. (help(strip_and_upper))

### Collections

* List
1. mutable, 변경가능하다.
2. 여러 데이터 타입이 한번에 들어갈 수 있지만 sort 등의 몇몇 함수 사용에 제약이 있다.

* Tuple
immutable, 변경불가능하다.

* Dictionary
1. 값은 Mutable, 변경 가능하다.
2. 유니크한 key값을 통해 value에 접근한다.

* Set
1. 중복을 허용하지 않고 순서가 없다. 따라서 인덱스로 접근이 불가능하다.
2. 딕셔너리와 비슷하게 생겼으나 Key 가 없는 상태와 같다.

---

## Class
class 명은 대체로 대문자로 시작한다

* 클래스 안에 있는 함수  -> 메서드(method) <br>
  ```def __int__```     -> 생성자(constructor) - 객체가 생성될 때 자동으로 실행된다.
  클래스 안에 함수 안에 선언된 변수  -> 인스턴스 변수
  클래스 안에 함수 밖에 선언된 변수  -> 클래스 변수

* 생성자가 없다면?
```python
class Empty:
    pass

E = Empty() 
```
문제 없다!

```python
class NoInit:
    def say_hello(self):
        print("Hello!!!!!!")


noinit = NoInit()
noinit.say_hello()
```
역시 문제 없다!
하지만 객체가 들고있어야 할 변수가 없기 때문에 단순히 return 하고 끝이다.
객체가 들고있을 변수를 설정해주고, 좀 더 형식에 맞추어주기 위해서는 생성자를 써주는 것이 좋다.

* ```___init___``` 
```python
class Empty:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello!!!!!!", self.name)


a = Empty("Jack")
a.__init__("Paul") # 가능하긴 하지만 이렇게 쓰진 않는다.
a.say_hello()
```

* 생성자에서 name을 지정하고 싶지 않다면?
```python
class Empty:
    def __init__(self):
        self.name = ""

    def set_name(self, name):
        # name 을 set 해주는 메소드
        self.name = name

    def say_hello(self):
        print("Hello!!!!!!", self.name)

a = Empty()
a.set_name('Paul')
a.say_hello()
```

* self
객체 자기 자신을 의미
Java 에서의 This 와 비슷하다.

```python
class Calc:
    add_count = 0 # 클래스 변수

    def __init__(self):
        self.total = 0 # 인스턴스 변수

    def add(self, num):
        Calc.add_count += 1
        self.total += num
        print("Total : ", self.total)


print(Calc.add_count) # 0
a = Calc()
b = Calc()
a.add(1)
a.add(1)
a.add(1)
print("-"*50)
b.add(2)
b.add(2)
b.add(2)
print(Calc.add_count) # 6
```

## Module
함수나 변수, 클래스를 모아놓은 파일 <br>
보통 .py 파일

* 모듈 사용방식 1: import 모듈파일이름. 해당 파일에 있는 전체 내용을 쓸 수 있다.
```python
import bmi
```
* 모듈 사용방식 2: from 모듈파일이름 import 모듈안의 함수
```python 
from bmi import calc_bmi
```
* 모듈 사용방식 3: from 모듈파일이름 import 모듈안의 함수 (변수 등 다양한 것이 가능) as 해당 모듈 별칭
```python
from bmi import calc_bmi as cb
from bmi import a, calc_bmi # a : bmi 파일 내 변수. 여러개를 불러올 때는 콤마로 구분한다. 
```

## 웹 크롤링
* 웹 브라우저 : HTML, CSS, JS 등의 언어로 이루어진 코드를 해석해서 실행하여 보여주는 역할을 한다.

* 크롬에서 웹 페이지 소스 바로 확인하기 : ctrl + shift + I
---
---

# 숙제

1. 기본 
: 복습 및 모르는 부분 질문
  네이버 API를 이용한 크롤링
  
2. 심화
: 네이버 급상승 검색어 크롤링 (이 부분은 API 제공을 해주지 않는다. 과연 어떻게 해야할까?)