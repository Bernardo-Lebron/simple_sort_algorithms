#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <chrono>
#include <iomanip>

void gnome_sort(std::vector<float>& arr) {
    int i = 0;
    while (i < (int)arr.size()) {
        if (i == 0 || arr[i] >= arr[i - 1]) {
            i++;
        } else {
            std::swap(arr[i], arr[i - 1]);
            i--;
        }
    }
}

/**
 * Função para carregar 'n' linhas do arquivo e medir o tempo de ordenação.
 */
double rodar_teste(const std::string& caminho_arquivo, int n) {
    std::vector<float> v;
    v.reserve(n);

    std::ifstream file(caminho_arquivo);
    if (!file.is_open()) {
        std::cerr << "Erro ao abrir: " << caminho_arquivo << std::endl;
        return -1.0;
    }

    std::string line;
    int count = 0;
    while (count < n && std::getline(file, line)) {
        if (!line.empty()) {
            v.push_back(std::stof(line));
            count++;
        }
    }
    file.close();

    auto start = std::chrono::high_resolution_clock::now();

    gnome_sort(v);

    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> diff = end - start;
    return diff.count();
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cout << "Uso: " << argv[0] << " <quantidade_elementos>" << std::endl;
        return 1;
    }

    int n = std::stoi(argv[1]);

    std::cout << "--- Iniciando Benchmark C++ (N: " << n << ") ---" << std::endl << std::endl;
    std::cout << std::fixed << std::setprecision(6);

    // TESTE 1: MELHOR CASO
    double d1 = rodar_teste("inputs/melhor_1000000.txt", n);
    if (d1 >= 0) {
        std::cout << "1. Crescente:     " << d1 << " segundos (Melhor caso)" << std::endl;
    }

    // TESTE 2: CASO MÉDIO
    double d2 = rodar_teste("inputs/medio_1000000.txt", n);
    if (d2 >= 0) {
        std::cout << "2. Aleatorio:     " << d2 << " segundos (Caso Médio)" << std::endl;
    }

    // TESTE 3: PIOR CASO
    double d3 = rodar_teste("inputs/pior_1000000.txt", n);
    if (d3 >= 0) {
        std::cout << "3. Decrescente:   " << d3 << " segundos (Pior caso)" << std::endl;
    }

    std::cout << "\n--- Testes concluidos ---" << std::endl;

    return 0;
}