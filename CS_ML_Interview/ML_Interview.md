# <span style='color:blue'>CS</span>

## big-O 표기법

$$f(x) = O(g(x))$$

모든 $x>=k$ 에 대하여 $f(x)<=cg(x)$ 를 만족하는 양의 상수 $c$와 $k$가 존재하면, $c$와 $k$는 함수 $f$에 대해 고정되어야 하고 $x$에 의존적이지 않아야 한다. 이 말은 $f(x)$가 $g(x)$의 어떤 상수를 곱한 것보다 작다는 뜻이며 점근적 상한에 대한 방법이다.

- $O(g(n))$은 $g(n)$의 증가율보다 작거나 같은 함수들의 집합이다.
  - 예를 들어 $O(n^2)$에는 $O(1)$, $O(n)$, $O(n\log n)$ 등이 포함된다.



## Linked LIst

장점:

- 동적 데이터 구조로 늘리거나 잘라내는 데 용이
- 데이터를 중간에 삽입하거나 제거하기 쉽다.

단점:

- 포인터를 저장해야 하기 때문에 일반 배열(array)보다 메모리를 더 사용한다.
- 데이터를 처음부터 순서대로 읽는다.



## 해쉬 테이블(Hash Table)

장점:

- $O(1)$ 탐색 방법 (최악의 경우 $O(n)$)
- 데이터 삽입 제거 용이

단점:

- 충돌 발생 가능성이 있음
- 최악의 경우 $O(n)$
- 키 딕셔너리 사이즈가 작으면 다음 포인터로 넘어가는 것이 중요
- 키를 해쉬 벨류로 저장해야 하기 때문에 일반 배열보다 메모리를 더 사용



## Binary Search Tree

이진탐색(binary search)과 연결리스트(linked list)를 결합한 자료구조

- 이진탐색의 탐색에 소요되는 계산복잡성은 $O(\log n)$으로 빠르지만 자료 입력, 삭제가 불가능

- 연결리스트의 자료 입력, 삭제에 필요한 계산복잡성은 $O(1)$로 효율적이지만 탐색하는데는 $O(n)$의 계산복잡성 발생

- 두 장점을 합쳐보자.

나무 모형의 데이터 구조로 왼쪽 자식 노드가 부모 노드보다 크면 오른쪽 자식 노드는 부모 노드보다 작다 (혹은 정반대).

중복된 노드가 없어야 함.

- 탐색 시 중위순회(inorder) 방식 사용. (왼쪽 서브트리 - 노드 - 오른쪽 서브트리 순으로 순회)

- 이렇게 하면 이진탐색트리 내의 모든 값을 정렬된 순서로 읽음

- 탐색: $O(h)$ 여기서 $h$는 트리의 높이

- 삽입: 탐색 + 연결리스트 삽입 ($O(1)$)

- 삭제: 

  1. 삭제 대상 노드의 오른쪽 서브트리를 찾는다.

  2. successor(1에서 찾은 서브트리의 최소값) 노드를 찾는다.

  3. 2에서 찾은 sucessor의 값을 삭제 대상 노드에 복사한다.
  4. successor 노드를 삭제한다.

  - 트리의 높이가 $h$이고 삭제 대상 노드의 레벨이 $d$라고 했을 때
  - 1번 탐색 과정에서 $d$번의 비교 연산
  - 2번 successor 노드를 찾기 위해서 $(h-d)$번의 비교 연산
  - 3번과 4번은 복사하고 삭제하는 과정으로 상수시간이 걸리기 때문에 무시해도 좋음
  - 종합적으로 $O(d+h-d)$ 즉 $O(h)$ 의 계산복잡도



## Heap

부모 노드는 자식 노드보다 항상 크거나 작다.

생성

1. 원소가 삽입되면 가장 밑단에서 생성될 수 있는 공간 중 가장 왼쪽에 노드가 생성된다.
2. 생성된 노드와 부모 노드를 비교하여 삽입된 노드가 크면 (혹은 작으면) 자식 노드와 부모 노드의 원소를 교환
3. 같은 방식으로 부모 노드와 자식 노드 교환
4. 시간복잡도는 최악의 경우 $O(\log n)$

삭제

- 큐이기때문에 삭제는 항상 루트노드에서 이루어진다.

1. 최하위 레벨 노드의 원소를 루트노드로 옮긴다. (기존 루트노드의 원소는 삭제)
2. 교환된 최상위 루트 노드와 그 자식 노드를 비교하고 위치가 올바르면 멈춘다.
3. 아니면 자식 노드와 교환한다. (max-heap이면 두 자식 노드 중 더 큰 자식 노드와 교환, min-heap이면 더 작은 자식 노드와 교환)
4. 변경된 자식 노드를 대상으로 2, 3번 과정을 반복한다.
5. 삭제도 시간복잡도는 $O(\log n)$

단점: 탐색 시에는 $O(n)$의 시간복잡도를 가진다.



## Heap vs Stack

스택은 메모리에 저장되고 CPU로 관리됨. 함수에서 새로운 변수를 선언할 때마다 해당 변수는 스택에 쌓임. (재귀함수같이 함수에서 함수를 호출할 때 호출된 함수가 먼저 실행되는 이유라고 봐야 하나봄) 함수가 종료되면 해당 함수에 의해 쌓인 변수는 스택에서 해재됨

스택에 올라갈 수 있는 변수의 크기에는 한계가 있음

힙은 임의의 위치에 객체가 생성됨 (dynamic allocation). 따라서 어떤 객체의 property에 값을 저장하거나 저장된 값을 가져오고 싶으면, 그 객체의 힙 영역상 좌표를 알고 있어야 함.

힙 영역에 생성한 변수는 블록을 빠져나와도 힙에 유지됨 (전역변수).

힙 영역을 두면 하나의 객체를 여러 참조변수에서 공유하는 형태로 사용할 수 있어 훨씬 메모리 공간을 절약할 수 있게 됨

다만 CPU에 의해 타이트하게 관리되지 않고 힙에 쓸 수 있는 변수 크기에 제한이 없기 때문에 memory leak 발생의 위험이 있음



## Garbage Collection

힙 영역은 매우 넓어서, 객체의 위치를 기억하는 참조 변수가 사라지면 사막 한 가운데 볼펜을 떨어뜨린 상황이 되어버림. 이렇게 쓰레기가 되어버린 객체는 가비지 컬렉션이라는 기능에 의해 소멸됨

mark-and-sweep

- Mark: GC roots로부터 모든 객체 참조를 검토하고 살아있는 객체를 마킹
- Sweep: 힙 메모리에 마킹되지 않은 객체가 차지하는 영역을 해제



## DFS (Depth First Search)

현재 정점에서 갈 수 있는 점들까지 들어가면서 탐색 (Stack and mark visited)



## BFS (Breadth First Search)

현재 정점에 연결된 가까운 점들부터 탐색 (Queue and mark visited)



## Compiler

코드를 한 언어에서 다른 언어로 변환하는 소프트웨어. 대부분 hign-level language에서 low-level language (machine code)로 변환한다.

- 프로그램 runtime 전에 전체 소스 코드를 검사하여 machine code로 변환
- 소스코드를 분석하는데 많은 시간이 들지만 전체 실행시간은 interpreter로 변환한 코드보다 비교적 빠르다.
- linking을 추가로 필요로 하는 중간 Object Code를 생성하여 더 많은 메모리를 필요로 한다.
- 전체 코드를 검사한 후에 오류 메세지를 생성. 프로그램 실행 전에 오류 발견이 가능
- C, C++, Java 등



## Interpreter

프로그램 언어로 쓰여진 대로 직접 실행하는 소프트웨어

- 프로그램 runtime에 한 번에 한 줄씩 변환한다.
- 소스코드를 분석하는데 걸리는 시간은 적지만 전체 실행시간은 Compiler보다 상대적으로 느림
- 중간 Object Code가 만들어지지 않아 메모리 효율이 높음
- 첫 오류를 만날 때까지 프로그램을 계속 번역하고 오류를 만나면 중지. 따라서 오류 발생 전에 실행된 코드가 있을 가능성이 높음
- Python, Ruby 등



## Object Oriented Programming (객체지향프로그래밍)

장점:

- 프로그램을 유연하고 변경이 용이하게 만든다.
- 프로그램의 개발과 보수를 간편하게 만든다.
- 직관적인 코드 분석을 가능하게 한다.



강한 응집력(Strong Cohesion)과 약한 결합력(Weak Coupling)을 지향

- 강한 응집력이란 프로그램의 한 요소가 특정 목적을 완수하기 위해 밀접하게 연관된 기능들로 구현되는 것을 의미
- 약한 결합력이란 프로그램의 한 요소가 다른 요소와 관계를 크게 맺고 있지 않는 것을 의미
- 요소의 군집별 분산이 작고 군집간 분산이 큰 프로그램이라고 이해하면 되러나?



OOP의 기본 구성 요소

- 클래스(Class)

  같은 종류의 집단에 속하는 속성과 행위를 정의한 것. 설계도 같은 것이라고 보면 됨

- 객체(Object)

  클래스의 인스턴스(Instance). 상위 클래스의 속성을 가지고 개별적인 특성과 행위(Method)를 가짐. 같은 설계도로 만들었으나 옵션이 서로 다른 자동차

- 메서드(Method)

  클래스로부터 생성된 객체를 사용하는 방법. 객체의 속성을 조작하는 데 사용. 자동차의 시동을 켠다, 속도를 낸다, 좌회전, 우회전 등



OOP의 특성

- 캡슐화(Encapsulation)

  객체의 데이터를 외부에서 직접 접근하지 못하게 막고, 함수를 통해서만 조작이 가능하게 하는 작업

  자동차의 속도 값을 직접 넣는 것이 아니라 엑셀과 브레이크를 밟아 조절하도록 하는 것과 같음

- 추상화(Abstraction)

  객체들이 가진 공통의 특성들을 파악하고 불필요한 특성들을 제거하는 과정

  자동차가 속도를 내기 위해 엔진이 돌아가고 동력을 바퀴에 전달하는 이러한 과정들은 사용자가 굳이 알 필요도 조작할 필요도 없다.

- 다형성(Polymorphism)

  같은 클래스에서 만들어진 객체여도 형태는 같으나 다른 기능을 가질 수 있다. 같은 종의 차더라도 옵션이 다를 수 있다.

- 상속(Inheriance)

  상위 개념의 클래스를 가지는 클래스의 객체는 상위 클래스의 속성과 메서드를 상속받음

  트럭은 자동차의 속성 (바퀴, 창문, 핸들 등) 을 가지고 있고 기능 (시동켜기, 속도조절, 좌우회전 등) 도 가지고 있다.



## Python Generator

iterator를 생성해주는 함수. 함수안에 yield 키워드를 사용한다.

- iterable한 순서가 지정된다.
- 느슨하게 평가된다. (무슨 의미일까?) (순서의 다음 값은 필요에 따라 계산된다.)
- 함수의 내부 로컬 변수를 통해 내부상태가 유지된다.
- 무한한 순서가 있는 객체를 모델링할 수 있다. (명확한 끝이 없는 Data stream 처리 가능)
- 자연스러운 stream 처리를 위 파이프라인으로 구성할 수 있다.



## Multi-Threading vs Multi-Processing

**Process**란 메모리에 적재되어 운영체제에 의해 실행중인 프로그램을 의미.

process들은 다시 **thread**라는 경량화된 프로세스로 나뉘어짐.

**Multi-Processing**은 실행되는 프로그램과 다른 프로그램 하나를 더 실행시켜서 동시에 처리

**Multi-Threading**은 thread를 여러 개 생성하여 동시에 처리

(그래서 `ps -ef | grep python` 으로 확인하면 멀티프로세싱은 python 프로세서가 추가적으로 더 나타나는 것을 확인 가능한가보다.)

python에서 멀티프로세싱을 사용한 이유는 파이썬에서 자원을 관리하기 위해 **Global Interpreter Lock(GIL)** 으로 두 쓰레드에서 공유하는 하나의 자원이 한쪽에서 점유중일 때 다른 쪽에서 사용하지 못하도록 되어있기 때문. 멀티프로세싱을 이용하면 이 문제가 해결된다.

그리고 나같은 경우에는 `ps -ef | grep python` 을 이용해서 한쪽 기능이 꺼졌는지 켜져있는지 확인하기 위해 멀티프로세싱을 이용했음..



## Python 3.8 추가사항

### 할당 표현식

- 기존 방식

    ```python
    title = item.get('title')
    if title:
        print(title)
    ```

- 할당 표현식을 사용한 방식

  ```python
  if title := item.get('title')
      print(title)
  ```

list comprehension에서도...

- 기존 방식

  ```python
  stuff = [(lambda y: [y, x/y])(f(x)) for x in range(5)]
  ```

- 할당 표현식을 사용한 방식

  ```python
  stuff = [[y := f(x), x/y] for x in range(5)]
  ```

  

### 위치 고정 파라미터

매서드나 함수의 특정 위치에서 정해진 파라미터만 받는 기능

```python
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
```

위 함수를 호출할 때...

```python
f(10, 20, 30, d=40, e=50, f=60)  # 호출 가능
f(10, b=20, 30, d=40, e=50, f=60)  # b는 키워드 전달인자가 될 수 없음
f(10, 20, 30, d=40, 50, f=60)  # e는 키워드 전달인자여야 함
```



### f-문자열에서 평가식(self-documenting expression)을 위한 =기호 추가

```python
name = 'jinoan'
print(f'name = {name}')  # name = jinoan
```

`name`을 두번 써야 한다.

이 기능을 사용하면 `name`을 한 번만 써도 됨.

```python
name = 'jinoan'
print(f'{name = }')  # name = jinoan
```

숫자 포맷도 지정 가능

```python
pi = 3.141592
print(f'{pi = :.3f}')  # pi = 3.141
trd = 3000
print(f'{trd = :,d}')  # trd = 3,000
```



## Python 3.9 추가사항

### 새로운 Dictionary 연산자

기존 dictionary 병합 방법

```python
d1 = {'x': 1, 'y': 4, 'z': 10}
d2 = {'a': 7, 'b': 9, 'x': 5}

# 예상되는 병합 결과
# {'x': 5, 'y': 4, 'z': 10, 'a': 7, 'b': 9}
# ('x'는 뒤에 오는 dictionary값으로 덮어쓰기 됨)

# 1.
d = dict(d1, **d2)

# 2.
d = d1.copy()
d.update(d2)

# 3.
d = {**d1, **d2}
```

새로운 dictionary 병합 방법

```python
d = d1 | d2

# in-place merging
d1 |= d2
```



### 유형 주석 업데이트

함수에서 list와 dict 같은 타입 유형을 지정하여 사용하기 용이해짐

```python
def greet_all(names: list[str]) -> None:
    for name in names:
        print('Hello', name)
```



### Module update

1. math

   math 모듈의 ged(최대공약수 계산) 기능 강화, lcm(최소공배수), nextafter(가장 근사한 부동 소수점 값 계산), ulp(부동 소수점의 가장 하위단 출력) 기능 추가

   ```python
   import math
   
   # Greatest common divisor
   math.gcd(80, 64, 152)  # result: 8
   
   # Least common mutiple
   math.lcm(4, 8, 5)  # result: 40
   
   # Next float after 4 going towards 5
   math.nextafter(4, 5)  # result: 4.000000000000001
   
   # Unit in the Last Place
   math.ulp(1000000000000000)  # result: 0.125
   ```

   

2. str

   접두사와 접미사를 제거하는 새로운 함수 추가

   ```python
   # 접두사 제거
   'someText'.removeprefix('some')  # result: 'Text'
   
   # 접미사 제거
   'someText'.removesuffix('Text')  # result: 'some'
   ```



3. http, ipaddress 지원

   http status code 몇 가지 추가

   ipaddress에서 IPv6Address 추가



4. functools

   functoos 모듈에서 topological sort 지원.

   ```python
   from functools import TopologicalSorter
   graph = {'A':{'D'}, 'B':{'D'}, 'C':{'E', 'H'}, 'D':{'F', 'G', 'H'}, 'E':{'G'}}
   ts = TopologicalSorter(graph)
   list(ts.static_order())  # result: ['H', 'F', 'G', 'D', 'E', 'A', 'B', 'C']
   ```

   

5. os

   os 모듈에 CLD_KILLEd, CLD_STOPPED 클래스가 추가됨. 자식 프로세스(child process)를 끝내거나 중지시키는게 가능해짐

   unsetenv()가 윈도우에서도 동작 가능해짐



6. xml

   xml, etree, ElementTree를 통해 XML 파일로 직렬화 할 때 이제 공백이 유지됨