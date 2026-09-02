#include <stdio.h>

int main(void) {

    struct Point {
        int x;
        int y;
    } typedef Point;

    typedef struct {
        int x;
        int y;
    } Point2;

    Point p1 = {1, 2};
    Point2 p2 = {3, 4};

    printf("p1: (%d, %d)\n", p1.x, p1.y);
    printf("p2: (%d, %d)\n", p2.x, p2.y);

    return 0;
}