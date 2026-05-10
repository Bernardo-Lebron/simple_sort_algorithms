#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void selectionSort(double arr[], int n) {
    int i, j, min_idx;
    double temp;
    for (i = 0; i < n - 1; i++) {
        min_idx = i;
        for (j = i + 1; j < n; j++)
            if (arr[j] < arr[min_idx]) min_idx = j;
        
        temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

int main(int argc, char *argv[]) {
    // Se houver um argumento no terminal, usa ele. Se não, usa 1000.
    int num_linhas = (argc > 1) ? atoi(argv[1]) : 1000; 
    
    double *data = (double *)malloc(num_linhas * sizeof(double));
    if (!data) { printf("Erro de memoria!\n"); return 1; }
    
    // Tentamos abrir o arquivo. Note que o Makefile entra na pasta 'c', 
    // então o caminho '../dados/aleatorio.txt' está correto.
    FILE *file = fopen("../dados/aleatorio.txt", "r"); 
    if (!file) { 
        printf("Erro ao abrir arquivo em c/selection!\n"); 
        free(data);
        return 1; 
    }

    for (int i = 0; i < num_linhas; i++) {
        if (fscanf(file, "%lf", &data[i]) == EOF) {
            num_linhas = i; // Ajusta caso o arquivo tenha menos linhas que o N solicitado
            break;
        }
    }
    fclose(file);

    clock_t start = clock();
    selectionSort(data, num_linhas);
    clock_t end = clock();

    printf("Tempo: %f s\n", (double)(end - start) / CLOCKS_PER_SEC);
    
    // Opcional: imprimir o menor valor para conferir o 133 (ou similar)
    if (num_linhas > 0) {
        printf("Menor valor encontrado: %.2f\n", data[0]);
    }

    free(data);
    return 0;
}