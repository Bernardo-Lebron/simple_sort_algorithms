#include <iostream>
#include <vector>
#include <fstream>
#include <chrono>
#include <string> // Para o stoi

using namespace std;

// Implementação do Selection Sort
void selectionSort(vector<double>& arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }
        // Troca usando a função padrão do C++
        swap(arr[min_idx], arr[i]);
    }
}

int main(int argc, char* argv[]) {
    // Captura o N do terminal. Se não existir, usa 1000.
    int num_linhas = (argc > 1) ? stoi(argv[1]) : 1000;
    
    vector<double> data;
    data.reserve(num_linhas); // Reserva memória para evitar realocações

    // Abre o arquivo (o caminho ../dados/aleatorio.txt está correto para o Makefile)
    ifstream file("../dados/aleatorio.txt");
    
    if (!file.is_open()) {
        cerr << "Erro ao abrir o arquivo dados!" << endl;
        return 1;
    }

    double valor;
    int cont = 0;
    // Lê exatamente N valores ou até o fim do arquivo
    while (cont < num_linhas && file >> valor) {
        data.push_back(valor);
        cont++;
    }
    file.close();

    // Medição de tempo com high_resolution_clock
    auto start = chrono::high_resolution_clock::now();
    selectionSort(data);
    auto end = chrono::high_resolution_clock::now();

    chrono::duration<double> diff = end - start;
    
    // Formato de saída para facilitar a leitura no benchmark
    cout << "Tempo: " << fixed<<  diff.count() << " s" << endl;
    if (!data.empty()) {
        cout << "Menor valor: " << data[0] << endl;
    }

    return 0;
}