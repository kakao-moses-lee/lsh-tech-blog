### Thread Safe 란?

멀티 스레드 프로그래밍에서 어떤 함수나 변수, 객체가 여러 스레드로부터 동시에 접근이 이루어져도 프로그램의 실행에 문제가 없음을 뜻한다. 
하나의 함수가 스레드로부터 호출되어 실행중일때, 다른 스레드가 그 함수를 호출하여 동시에 실행되더라도 각 스레드에서 함수의 수행결과가 올바로 나오는 것을 정의한다. 

```python
# 여러 스레드에서 코드를 동시에 실행하더라도 
# 각 스레드에서 출력되는 값이 5로 동일하다면
# thread - safety 하다고 할 수 있다. 
a = 3
b = 2
print(a + b)
```

```python
# 딕셔너리의 조회와 대입 사이에 스레드 전환이 일어날 수 있기때문에 
# thread - safety 하지 않다. 
dict = {}
dict[key] += value
dict[key] = dict[key] + value
dict[key] = dict[key2]
```



**Thread Safe 를 지키기위한 방법**

1. Re-entry : 어떤 함수가 한 스레드에 의해 호출되어 실행 중일때, 다른 스레드가 그 함수를 호출하더라도 그 결과가 각각 올바로 주어져야 한다. 

2. Thread-local storage : 공유 자원의 사용을 최대한 줄여 각각의 스레드에서만 접근 가능한 저장소들을 사용함으로써 동시 접근을 막는다.
   이 방식은 **동기화** 방법과 관련되어 있고, 또한 공유상태를 피할 수 없을 때 사용하는 방식이다.
   => 멀티 스레드 환경에서 전역변수 사용을 지양하라.  

3. Mutual exclusion : 공유 자원을 꼭 사용해야 할 경우 해당 자원의 접근을 세마포어 등의 락으로 통제한다.
   => 동기화 객체, python 의 경우 (threading.Lock)

4. Atomic operations : 공유 자원에 접근할 때 원자 연산을 이용하거나 '원자적'으로 정의된 접근 방법을 사용함으로써 상호 배제를 구현할 수 있다.

    

#### 결론

- Thread Safety 를 지키기 위해서 동기화 객체(Mutual exclusion == **GIL**) 을 사용하는 것이 좋다. (1, 2, 4 는 고려하기 쉽지 않기 때문. 
- GIL 이 필요한 이유 : CPython 의 메모리 관리가 thread-safe 하지 않기 떄문. 

    

### Thread 동기화란 ? 

- 실행순서의 동기화
- 메모리 접근의 대한 동기화 

**실행순서의 동기화**

스레드의 실행순서를 정의하고, 반드시 이 순서를 따르도록 하는 것이다.

**메모리 접근에 대한 동기화**

데이터 영역과 힙 영역과 같이 한 순간에 하나의 쓰레드만 접근하도록 하는 것이 메모리 접근에 대한 동기화이다.
만약 두 개의 쓰레드가 **동시에 데이터에 접근**하여 변경한다면 계산 결과가 덮여씌워 지는 등 여러 문제가 발생할 수 있다.

**동기화를 위한 방법**

- User Mode 동기화
- Kernel Mode 동기화



### 유저 모드 동기화

1. 유저 모드 동기화 (User Mode Synchronize)

- 동기화가 진행되는 과정에서 커널의 힘을 빌리지 않는 (커널 코드가 실행되지 않는) 동기화 기법이다.
- 따라서 동기화를 위해서 커널 모드로의 전환이 불필요해 성능상의 이점이 있다.
- 그러나 그만큼 기능상의 제한도 있다.
- **Ex) 크리티컬 섹션 기반의 동기화, 인터락 함수 기반의 동기화**

### 커널 모드 동기화

1. 커널 모드 동기화 (Kernel Mode Synchronize)

- 커널에서 제공하는 동기화 기능을 활용하는 방법이다.
- 따라서 동기화에 관련된 함수가 호출될 때마다 커널 모드로의 변경이 필요하고, 이는 성능의 저하로 이어지게 된다.
- 하지만 그만큼 유저 모드 동기화에서 제공하지 못하는 기능을 제공받을 수 있다.
- **Ex) 뮤텍스 기반의 동기화, 세마포어 기반의 동기화, 이름있는 뮤텍스 기반의 프로세스 동기화, 이벤트 기반의 동기화**