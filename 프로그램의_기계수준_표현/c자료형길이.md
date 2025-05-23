# X86-64에서 c 자료형의 길이

물론입니다. 아래는 **정수 레지스터(Integer Register)**에 대한 정리입니다.
---

# 📌 정수 레지스터(Integer Register) 
- 정수 레지스터는 **CPU 내부에 있는 레지스터 중에서, 정수 데이터를 저장하고 처리하는 용도**로 사용되는 레지스터입니다.  
컴퓨터가 수행하는 대부분의 연산(덧셈, 뺄셈, 논리연산 등)은 이 정수 레지스터를 기반으로 합니다.
---

### ✅ 주요 기능  
| 기능 | 설명 |
|------|------|
| **산술 연산** | 덧셈, 뺄셈, 곱셈, 나눗셈 등 정수 연산 수행 시 피연산자 또는 결과값을 저장 |
| **논리 연산** | AND, OR, XOR, NOT 등 비트 단위 논리 연산에 사용 |
| **자료 저장/이동** | 메모리에서 데이터를 가져와 일시적으로 저장하거나 다른 레지스터로 전달 |
| **주소 계산** | 포인터 연산이나 배열 인덱스 계산 시 정수 레지스터를 사용하여 주소 계산 |

---

### ✅ 예시 (x86-64 아키텍처 기준)
| 레지스터 | 설명 |
|----------|------|
| `rax` | 누산기(A) - 산술 연산 결과 주로 저장 |
| `rbx` | 기준 레지스터(B) - 데이터 저장 및 참조용 |
| `rcx` | 카운터(C) - 반복문, 루프 연산 등에 사용 |
| `rdx` | 데이터(D) - 입출력 연산, 곱셈/나눗셈 결과 저장 |
| `rsi`, `rdi` | 문자열 조작, 함수 인자 전달 등에 사용 |
| `rsp`, `rbp` | 스택 포인터 / 베이스 포인터 (메모리 참조에 관여) |

> `r`은 64비트, `e`는 32비트, `ax`, `bx` 등은 16비트 버전

---

### ✅ 정수 레지스터 vs 부동소수점 레지스터  
| 구분 | 정수 레지스터 | 부동소수점 레지스터 |
|------|----------------|----------------------|
| 데이터 형태 | 정수 | 실수 (소수 포함) |
| 사용 목적 | 일반 연산, 주소계산 등 | 실수 연산 (과학/공학 계산 등) |
| 대표 예시 | `rax`, `rbx`, `rcx`, ... | `xmm0`, `xmm1`, `st0`, ... |

---

### ✅ 참고  
- **레지스터는 CPU에서 가장 빠른 기억장소**입니다.  
- **연산에 직접 관여하므로**, 컴파일러나 어셈블리 코드를 보면 레지스터가 빈번하게 등장합니다.

---

필요하시면 ARM, RISC-V, MIPS 등의 아키텍처 기준으로도 예시 추가해드릴 수 있어요!