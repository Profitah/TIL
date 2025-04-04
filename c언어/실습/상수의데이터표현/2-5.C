#include <stdio.h>

int main(void)
{
    printf("%d\n", 12);     // 10진수 정수 상수 출력
    printf("%d\n", 014);    // 8진수 정수 상수 출력 (014 = 10진수 12)
    printf("%d\n", 0xc);    // 16진수 정수 상수 출력 (0xc = 10진수 12)

    return 0;
}
