#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void gnome_sort(int arr[], int n) {
    int i = 0;
    while (i < n) {
        if (i == 0 || arr[i] >= arr[i - 1]) {
            i++;
        } else {
            int temp = arr[i];
            arr[i] = arr[i - 1];
            arr[i - 1] = temp;
            i--;
        }
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Uso: %s <arquivo.txt>\n", argv[0]);
        return 1;
    }

    FILE *f = fopen(argv[1], "r");
    if (!f) {
        fprintf(stderr, "Erro ao abrir arquivo: %s\n", argv[1]);
        return 1;
    }

    int capacity = 1024;
    int n = 0;
    int *arr = malloc(capacity * sizeof(int));

    int x;
    while (fscanf(f, "%d", &x) == 1) {
        if (n == capacity) {
            capacity *= 2;
            arr = realloc(arr, capacity * sizeof(int));
        }
        arr[n++] = x;
    }
    fclose(f);

    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);

    gnome_sort(arr, n);

    clock_gettime(CLOCK_MONOTONIC, &end);

    double ms = (end.tv_sec - start.tv_sec) * 1000.0
              + (end.tv_nsec - start.tv_nsec) / 1e6;

    printf("  n=%-8d  tempo: %.4f ms\n", n, ms);

    free(arr);
    return 0;
}
