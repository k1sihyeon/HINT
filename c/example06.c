#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 10

void reverseArray(int a[], int size);
void printArray(int a[], int size);

int main(void) {
    int arr[SIZE];
    int i;

    // random init
    srand(time(NULL));
    for (i = 0; i < SIZE; i++) {
        arr[i] = rand() % 100;
    }

    // print
    printf("Original Array:\n");
    printArray(arr, SIZE);

    // reverse
    reverseArray(arr, SIZE);

    // print reversed
    printf("Reversed Array:\n");
    printArray(arr, SIZE);

    return 0;
}

void reverseArray(int a[], int size) {
    int tmp;
    for (int i = 0; i < size / 2; i++) {
        tmp = a[i];
        a[i] = a[size - 1 - i];
        a[size - 1 - i] = tmp;
    }

    return;
}

void printArray(int a[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");

    return;
}