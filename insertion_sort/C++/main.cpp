#include <iostream>
#include <vector>
#include <fstream>
#include <chrono>

using namespace std;

void insertionSort(vector<int>& arr) {
    for (int i = 1; i < (int)arr.size(); i++) {
        int chave = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > chave) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = chave;
    }
}

double rodar_teste(const string& arquivo, int n) {
    ifstream f(arquivo);
    if (!f.is_open()) return -1.0;

    vector<int> v;
    int x;
    while (f >> x && (int)v.size() < n) v.push_back(x);
    f.close();

    auto start = chrono::high_resolution_clock::now();
    insertionSort(v);
    auto end = chrono::high_resolution_clock::now();

    return chrono::duration<double>(end - start).count();
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        cout << "Uso: " << argv[0] << " <n_elementos>" << endl;
        return 1;
    }

    int n = stoi(argv[1]);
    cout << "--- Iniciando Benchmark Insertion Sort (N: " << n << ") ---" << endl << endl;

    double d1 = rodar_teste("crescente.txt", n);
    if (d1 >= 0) printf("1. Crescente:   %.6f segundos (Melhor caso)\n", d1);

    double d2 = rodar_teste("aleatorio.txt", n);
    if (d2 >= 0) printf("2. Aleatorio:   %.6f segundos (Caso Medio)\n", d2);

    double d3 = rodar_teste("decrescente.txt", n);
    if (d3 >= 0) printf("3. Decrescente: %.6f segundos (Pior caso)\n", d3);

    cout << endl << "--- Testes concluidos ---" << endl;
    return 0;
}