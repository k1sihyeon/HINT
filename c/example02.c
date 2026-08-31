#include <stdio.h>

int main(void) {
    int num;
    char nChar;

    printf("양의 정수를 입력 >> ");
    int chk = scanf("%d%c", &num, &nChar);

    if ((num <= 0) || (chk != 2) || (nChar != '\n')) {
        printf("양의 정수를 입력하세요.\n");
        return 1;
    }

    if (num % 3 == 0) {
        printf("3 6 9! 짝!\n");
    }
    else {
        printf("3 6 9! 해당하지 않음\n");
    }

    return 0;
}