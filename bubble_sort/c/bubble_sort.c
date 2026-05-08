#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

void bubbleSort(float *nums, int n) {
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (nums[j] > nums[j + 1]) {
                float temp = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped) break; 
    }
}

// Função auxiliar para carregar dados e medir o tempo
double rodar_teste(const char *arquivo, int n) {
    float *v = (float *)malloc(n * sizeof(float));
    FILE *f = fopen(arquivo, "r");
    if (!f || !v) {
        if(v) free(v);
        return -1.0;
    }

    char line[1024];
    int count = 0;
    while (count < n && fgets(line, sizeof(line), f)) {
        if (sscanf(line, "%f", &v[count]) == 1) count++;
    }
    fclose(f);

    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);
    
    bubbleSort(v, count);
    
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
    printf("--- Iniciando Benchmark (N: %d) ---\n\n", n);


    // TESTE 1: MELHOR CASO
    double d1 = rodar_teste("crescente.txt", n);
    if (d1 >= 0) printf("1. Crescente:     %.6f segundos (Melhor caso)\n", d1);

    // TESTE 2: CASO MÉDIO
    double d2 = rodar_teste("aleatorio.txt", n);
    if (d2 >= 0) printf("2. Aleatorio:     %.6f segundos (Caso Médio)\n", d2);

    // TESTE 3: PIOR CASO
    double d3 = rodar_teste("decrescente.txt", n);
    if (d3 >= 0) printf("3. Decrescente:   %.6f segundos (Pior caso)\n", d3);

    printf("\n--- Testes concluidos ---\n");
    return 0;
}