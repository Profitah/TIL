#include <stdio.h>

int main(void)
{
    int a;         // 일반 변수 선언
    int *pa;       // int형 포인터 변수 선언

    pa = &a;       // 포인터에 a의 주소 대입
    *pa = 10;      // 포인터가 가리키는 곳(a)에 10 저장

    printf("포인터로 a 값 출력 : %d\n", *pa);
    printf("변수명으로 a 값 출력 : %d\n", a); // 변수 a의 값 출력

    return 0;
}















