#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

double get_time() {
    struct timeval t;
    gettimeofday(&t, NULL);

    return t.tv_sec + t.tv_usec / 1000000.0;
}

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

int main() {

    FILE *file = fopen(
        "C:\\Users\\Arthur\\Desktop\\AEDS TRAB 2\\aleatorio.txt",
        "r"
    );

    if (!file) {
        printf("Erro ao abrir arquivo\n");
        return 1;
    }

    

    int limite = 1000000;

    int *numeros = malloc(limite * sizeof(int));

    if (numeros == NULL) {
        printf("Erro de memoria\n");
        return 1;
    }


    int cont = 0;

    while (cont < limite &&
           fscanf(file, "%d", &numeros[cont]) == 1) {

        cont++;
    }

    fclose(file);


    double start = get_time();

    insertionSort(numeros, cont);

    double end = get_time();

    printf("Tempo: %f segundos\n", end - start);

   
    free(numeros);

    return 0;
}