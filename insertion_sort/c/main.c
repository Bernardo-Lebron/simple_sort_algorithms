#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int chave = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > chave) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = chave;
    }
}

double rodar_teste(const char *arquivo, int n) {
    int *v = (int *)malloc(n * sizeof(int));
    FILE *f = fopen(arquivo, "r");
    if (!f || !v) {
        if (v) free(v);
        return -1.0;
    }

    int count = 0;
    while (count < n && fscanf(f, "%d", &v[count]) == 1) count++;
    fclose(f);

    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);

    insertionSort(v, count);

    clock_gettime(CLOCK_MONOTONIC, &end);

    double tempo = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
    free(v);
    return tempo;
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Uso: %s <n_elementos>\n", argv[0]);
        return 1;
    }

    int n = atoi(argv[1]);
    printf("--- Iniciando Benchmark Insertion Sort (N: %d) ---\n\n", n);

    double d1 = rodar_teste("crescente.txt", n);
    if (d1 >= 0) printf("1. Crescente:   %.6f segundos (Melhor caso)\n", d1);

    double d2 = rodar_teste("aleatorio.txt", n);
    if (d2 >= 0) printf("2. Aleatorio:   %.6f segundos (Caso Medio)\n", d2);

    double d3 = rodar_teste("decrescente.txt", n);
    if (d3 >= 0) printf("3. Decrescente: %.6f segundos (Pior caso)\n", d3);

    printf("\n--- Testes concluidos ---\n");
    return 0;
}