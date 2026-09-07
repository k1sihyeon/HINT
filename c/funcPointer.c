#include <stdio.h>

int add(int, int);
int sub(int, int);

int main(void) {
    int result;
    int (*pf)(int, int);
    void (*pf_void)(void);

    pf_void = (void(*)(void))add;
    result = ((int (*)(int, int))pf_void)(10, 20);
    printf("add: %d\n", result);

    pf = add;
    result = pf(10, 20);
    printf("add: %d\n", result);

    pf = sub;
    result = pf(10, 20);
    printf("sub: %d\n", result);

    return 0;
}

int add(int x, int y) {
    return x + y;
}

int sub(int x, int y) {
    return x - y;
}