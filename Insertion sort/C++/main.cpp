#include <iostream>
#include <vector>
#include <fstream>
#include <chrono>

using namespace std;

void insertionSort(vector<int>& arr) {
    for (int i = 1; i < arr.size(); i++) {
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
    vector<int> numeros;
    int valor;

    ifstream file("C:/Users/Arthur/Desktop/AEDS TRAB 2/aleatorio.txt");

    int limite = 1000000; // quantidade desejada

    while (file >> valor && numeros.size() < limite) {
        numeros.push_back(valor);
    }

    file.close();

    auto start = chrono::high_resolution_clock::now();

    insertionSort(numeros);

    auto end = chrono::high_resolution_clock::now();

    chrono::duration<double> diff = end - start;

    cout << "Tempo: " << diff.count() << " segundos" << endl;

    return 0;
}