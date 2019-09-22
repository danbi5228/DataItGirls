# Python Basic class 1

* 변수 : 숫자, 문자열 등의 값을 가리키는 것.
값을 가지고 있는 공간 이라는 표현을 하기도 하지만 파이썬에서는 '공간'이라는 것은 엄밀히 따지면 '틀린'표현이다.

* cmd 에서 repl -> python 입력
python 입력 창에서 나오기 -> quit() or exit() 입력
한 줄 확인하는 용으로 repl 환경을 자주 이용하는 것을 추천!!!

* a = 10
: 여기서 a는 10을 가리키는 것에 불과하므로 id(a) 해도 a가 저장된 주소값이 아니라 a가 가리키는 것의 주소값을 return

* built-in functions = 내장함수

* 리스트에서 삭제 방법
del - 해당 위치의 값 삭제. 파이썬 내장함수
remove - list 첫 번째 값부터 확인하면서 같은 값을 찾으면 삭제(같은 값이 여러개일 경우 가장 앞에 있는 값이 삭제). 리스트 멤버함수

* print 함수 뒤 end = '' 해주면 여러개의 print 함수를 써도 이어서 print 된다
print함수가 원래는 맨 뒤에 \n 을 추가하여 print를 했는데 만약 이렇게 하고 싶지 않다면 end인자를 이용해 추가하지 않도록 할 수 있다

* for 문 반대로 확인할 때
: for i in range(10, 1, -1)

* for 문 2개씩 건너뛸 때
: for i in range(1, 10, 2)

* for 문 반대로 확인하면서 2개씩 건너뛸 때
: for i in range(10, 1, -2)

* 논리 연산에서도 += 과 같은 줄임 표현이 가능하다
a = True
a &= False
print(a) --> False

* ctrl + c : 강제 실행종료
