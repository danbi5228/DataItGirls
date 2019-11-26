## 2019-11-25 Binary Search Tree

### 지난 수업 복습
* 객체 : 데이터(속성, 상태)와 프로시저(연산, 메서드)를 캡슐화한 것
* 인터페이스 : 프로시저의 signature 모음
* 클래스 : 인터페이스의 구현

### Binary Search Tree
* Data
    * Value
    * Children
* Interface
    * 객체 생성 (w/ value)
    * 트리에 값 추가 = 자녀 노드 생성
    * 트리에서 값 찾기

* Example
    * 연락처 (이름, 전화번호)
    * Jane. 010-1234-5678
    * Tom. ~~
    * Susan. ~~

    * 특정 사람을 찾아서 연락처를 보고자 한다면: 이름첫글자, 이름 순 확인
    * 빠르게 찾도록 만드는 데 BST 이용
    * 전체를 다 볼 필요 없이 건너뛰도록 만드는 것