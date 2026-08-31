#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    int arr[4][4];
    int i, j;
    int sum;
    double avg;

    // random init
    srand(time(NULL));
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
            arr[i][j] = rand() % 100;
        }
    }

    // avg
    sum = 0;
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
            sum += arr[i][j];
        }
    }
    avg = (double)sum / 16;

    // print
    printf("2D Array:\n");
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    // print - avg
    printf("Average: %.2f\n", avg);

    return 0;
}