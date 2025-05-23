# 📌 `sizeof`와 포인터 크기 정리
## ✅ 1. `sizeof(포인터 변수)`  
> 포인터 자체(주소)의 크기를 알려줌

```c
int* p;
printf("%lu\n", sizeof(p)); 
```

- **주소 크기**는 시스템에 따라 달라짐:
  - 32비트 시스템: 4바이트  
  - 64비트 시스템: 8바이트

📌 포인터가 어떤 자료형을 가리키든, **주소 크기는 항상 동일**

```c
char* pc;
int* pi;
double* pd;

sizeof(pc);  // 4 또는 8
sizeof(pi);  // 4 또는 8
sizeof(pd);  // 4 또는 8
```
---
## ✅ 2. `sizeof(*포인터)`  
> 포인터가 **가리키는 대상의 크기**를 알려줌
```c
int a = 10;
int* p = &a;

printf("%lu\n", sizeof(*p));  
```

| 표현 | 의미 |
|------|------|
| `sizeof(p)` | 포인터 자체의 크기 (주소 공간) |
| `sizeof(*p)` | `p`가 가리키는 값의 크기 (자료형 크기) |

예:

```c
char* pc;      // → sizeof(*pc) == 1
int* pi;       // → sizeof(*pi) == 4
double* pd;    // → sizeof(*pd) == 8
```

---

## ✅ 3. 비교 예제

```c
#include <stdio.h>

int main() {
    int a = 10;
    int* p = &a;

    printf("sizeof(p) = %lu\n", sizeof(p));   
    printf("sizeof(*p) = %lu\n", sizeof(*p)); 
```

🧠 결과 (64비트 환경 기준):
```
sizeof(p) = 8
sizeof(*p) = 4
```
---

## ✅ 4. 배열과 포인터에서의 주의점

```c
int arr[5] = {1, 2, 3, 4, 5};
int* p = arr;

sizeof(arr);   // 배열 전체 크기: 5 × 4 = 20
sizeof(p);     // 포인터 크기: 8 (64비트 기준)
sizeof(*p);    // 가리키는 값 크기: 4
```
📌 `arr`는 배열이고, `p`는 포인터니까 `sizeof` 결과가 다릅니다!
---

## ✅ 핵심 요약 표

| 표현 | 설명 | 예시 (64비트 기준) |
|------|------|---------------------|
| `sizeof(p)` | 포인터 자체의 크기 (주소) | 8 |
| `sizeof(*p)` | 포인터가 가리키는 값의 크기 | 자료형에 따라 다름 |
| `sizeof(arr)` | 배열 전체의 크기 | `int arr[5]` → 20 |
| `sizeof(&a)` | 주소값의 크기 | 8 |
| `sizeof(char*)`, `sizeof(int*)` | 모두 동일 (주소니까) | 8 |

---

좋아요! 올려주신 문제는 **포인터와 `sizeof` 연산자**에 관련된 문제입니다.  
차근차근 분석하고, **정답이 왜 그렇게 되는지**까지 설명드릴게요.
---

## ✅ 문제 요약
주소 크기가 **4바이트**일 때, 다음 중 `sizeof` 연산의 결과값이 **가장 큰 것**은?

```c
char *pc;
double *pd;
```

| 선택지 | 의미 |
|--------|------|
| ① `sizeof(pc)`      | `char*` 포인터 자체의 크기 |
| ② `sizeof(pd)`      | `double*` 포인터 자체의 크기 |
| ③ `sizeof(*pc)`     | `char` 자료형의 크기 |
| ④ `sizeof(*pd)`     | `double` 자료형의 크기 |
---

## ✅ 각각 분석

| 표현 | 해석 | 결과값 |
|------|------|--------|
| ① `sizeof(pc)` | `char*` 포인터의 크기 | **4** |
| ② `sizeof(pd)` | `double*` 포인터의 크기 | **4** |
| ③ `sizeof(*pc)` | `*pc`는 `char` → char의 크기 | **1** |
| ④ `sizeof(*pd)` | `*pd`는 `double` → double의 크기 | **8** ✅

---

## ✅ 정답

👉 **④ sizeof(*pd)** = 8 (가장 큼)

---

## 📌 포인트 정리

- `sizeof(포인터변수)` → 포인터 자체 크기 (주소 크기) → **4바이트**  
- `sizeof(*포인터변수)` → 포인터가 가리키는 **자료형 크기**  
  - `*pc` → `char` → 1바이트  
  - `*pd` → `double` → 8바이트

---

### 1. 포인터의 정의에 대해 알게 됨  
- 포인터는 **다른 변수의 메모리 주소를 저장하는 변수**이다.  
- 일반 변수는 값을 저장하지만, 포인터는 그 **변수의 주소** 를 저장한다.  
---
### 2. 포인터를 선언하고 값을 불러오는 방법에 대해 알게 됨  
- 포인터 선언 시에는 `*`를 사용한다. 예: `int *p;`  
- `&` 연산자(앤드퍼센트_연산자)는 변수의 **주소**를 구할 때 사용한다. 예: `p = &a;`  
- `*` 연산자(스타_연산자)는 **역참조** 연산자라고 불리며, 포인터가 가리키는 **주소의 실제 값**에 접근할 때 사용한다. 예: `*p`
- 포인터는 동시 선언이 가능함.
- 하나의 포인터는 한 번에 하나의 값(주소)만 가리킬 수 있음.
---

### 3. 포인터 선언 vs 역참조 연산자의 차이점에 대해 조사함

| 구분       | 의미                         | 사용 시점        | 출력문에서 사용 가능 여부     |
|------------|------------------------------|------------------|-------------------------------|
| `int *p;`  | 포인터 선언                  | 변수 선언 시     | ❌ 사용 불가 (출력 의미 없음) |
| `*p`       | 역참조 (주소의 값을 사용)    | 실행 중 언제든지 | ✅ 사용 가능 (출력/연산 등)   |

- 포인터 선언은 **변수 선언부**에서만 사용된다.
- `*p`는 코드 실행 중에 **p가 가리키는 주소의 실제 값을 가져오거나 변경**한다.
- 즉, `*`는 포인터를 **"선언할 때"와 "사용할 때" 역할이 다르다.**


좋습니다! 이번에는 포인터와 관련해서 자주 보게 되는 16진수(헥사) 표현 + 0x 접두사에 대해 더 깊이 있게 설명드릴게요.

📘 16진수 + 0x 접두사 상세 설명

✅ 1. 16진수(Hexadecimal)란?
숫자 16을 밑(base)으로 하는 수 체계, 즉 0부터 15까지 한 자리에 표현하는 진법
10진수	2진수	16진수
0	0000	0
1	0001	1
...	...	...
10	1010	A
11	1011	B
12	1100	C
13	1101	D
14	1110	E
15	1111	F
즉, 16진수는 0~9, A~F를 사용합니다.

✅ 2. 0x 접두사란?
C 언어에서 정수 리터럴이 16진수임을 나타내는 표식
* 0x 또는 0X를 숫자 앞에 붙이면 컴파일러는 그 수를 16진수로 인식합니다.
예시:
int a = 0x2A;   // 16진수 2A → 10진수로는 42
표현	의미
0x2A	16진수 2A (2×16 + A=10 → 42)
0xFF	255
0x0	0
✅ 3. 왜 포인터(주소)는 16진수로 표현할까?
* 메모리는 이진수로 구성되어 있음 (예: 64비트 시스템이면 64자리)
* 사람이 읽기엔 2진수는 너무 길고 복잡 → 16진수는 가독성이 좋음
* 1개의 16진수 = 4개의 2진수 → 딱 맞아떨어짐
예:
이진수:   0000 0000 1010 1111
16진수:   0x00AF
포인터는 실제로는 숫자지만, 메모리 주소이기 때문에 항상 16진수로 출력되는 게 일반적입니다.

✅ 4. %p의 출력 형태
int a = 10;
int* p = &a;
printf("%p\n", p);    // 예: 0x7ffeebf4c4ac
포인터 값	설명
0x	16진수임을 나타냄
7ffeebf4c4ac	메모리 주소 (플랫폼/운영체제에 따라 다름)
📌 포인터는 그 자체가 메모리 주소이므로 int나 float와 다르게 반드시 주소값으로서 16진수 출력이 필요합니다.

✅ 5. 참고: 16진수 출력 직접 해보기
int a = 42;
printf("%x\n", a);   // 소문자 16진수 출력 → 2a
printf("%X\n", a);   // 대문자 16진수 출력 → 2A
printf("0x%X\n", a); // 접두사 포함 출력 → 0x2A

🧠 기억 포인트
포인트	설명
포인터는 주소 → 주소는 메모리 위치 → 메모리 표현은 16진수	
0x는 C언어에서 "이건 16진수 숫자야"라는 표식	
%p로 포인터 출력하면 항상 0x가 붙은 16진수 형태	
직접 출력 시 %x, %X, 0x 조합으로 원하는 형식 만들 수 있음	
추가로 원하시면:
* 16진수 ↔ 10진수 변환하는 법
* 0x 없이 16진수 출력하는 방법
* 포인터 연산 시 16진수 주소가 어떻게 바뀌는지 예시 도 자세히 설명드릴 수 있어요!

좋습니다! 문제의 코드를 분석해서 어떤 값이 출력되는지 한 줄씩 추적하며 설명해드릴게요.

✅ 문제 코드
int a = 10, b = 20;
int *pa = &a, *pb = &b, *pt;

pt = pa;
pa = pb;
pb = pt;

printf("%d, %d", *pa, *pb);

✅ 변수 초기 상태
변수	값
a	10
b	20
pa	&a (→ 10)
pb	&b (→ 20)
pt	(초기화 안 됨)
✅ 실행 순서 분석
1. pt = pa; → pt는 &a를 가짐 (10을 가리킴)
2. pa = pb; → pa는 &b로 바뀜 (20을 가리킴)
3. pb = pt; → pb는 pt가 가지고 있던 주소, 즉 &a로 바뀜 (10을 가리킴)

✅ 최종 포인터 상태
포인터	가리키는 값
pa	&b → 20
pb	&a → 10
✅ 출력문
printf("%d, %d", *pa, *pb);
→ *pa = 20 → *pb = 10

✅ 정답 출력
20, 10