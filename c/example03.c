#define _USE_MATH_DEFINES

#include <stdio.h>
#include <math.h>

int main(void) {

    double humanHeight;
    double toTreeDist;
    double angle;

    double treeHeight;

    printf("사람의 키를 입력하세요(m) >> ");
    scanf("%lf", &humanHeight);
    
    printf("나무까지의 거리를 입력하세요(m) >> ");
    scanf("%lf", &toTreeDist);

    printf("나무와 사람 사이의 각도를 입력하세요(도) >> ");
    scanf("%lf", &angle);

    double radian = angle * M_PI / 180.0;
    treeHeight = humanHeight + toTreeDist * tan(radian);

    printf("나무의 높이는 %lf m입니다.\n", treeHeight);

    return 0;
}