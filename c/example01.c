#include <stdio.h>

int main(void) {
    int a, b, c, d;
    int tmp1, tmp2, tmp3 = 0;

    scanf("%d %d %d %d", &a, &b, &c, &d);

    if (a > b) {
        tmp1 = a;
    }
    else {
        tmp1 = b;
    }

    if (c > d) {
        tmp2 = c;
    }
    else {
        tmp2 = d;
    }

    if (tmp2 > tmp1) {
        tmp3 = tmp2;
    }
    else {
        tmp3 = tmp1;
    }

    printf("%d\n", tmp3);

    return 0;
}