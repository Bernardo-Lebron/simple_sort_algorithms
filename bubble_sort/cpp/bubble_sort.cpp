#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <chrono>
#include <iomanip>
#include <algorithm> // Para std::swap

/**
 * Bubble Sort O(n^2)
 * Com a otimização de parada antecipada (bool swapped).
 */
void bubble_sort(std::vector<float>& nums) {
    int n = nums.size();
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (nums[j] > nums[j + 1]) {
                std::swap(nums[j], nums[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break; // Melhor caso: O(n)
    }
}

/**
 * Função para carregar 'n' linhas do arquivo e medir o tempo de ordenação.
 */
double rodar_teste(const std::string& caminho_arquivo, int n) {
    std::vector<float> v;
    v.reserve(n); // Reserva memória de uma vez para ganhar performance

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

    // Início da medição de tempo
    auto start = std::chrono::high_resolution_clock::now();
    
    bubble_sort(v);
    
    auto end = std::chrono::high_resolution_clock::now();
    // Fim da medição

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
    double d1 = rodar_teste("crescente.txt", n);
    if (d1 >= 0) {
        std::cout << "1. Crescente:     " << d1 << " segundos (Melhor caso)" << std::endl;
    }

    // TESTE 2: CASO MÉDIO
    double d2 = rodar_teste("aleatorio.txt", n);
    if (d2 >= 0) {
        std::cout << "2. Aleatorio:     " << d2 << " segundos (Caso Médio)" << std::endl;
    }

    // TESTE 3: PIOR CASO
    double d3 = rodar_teste("decrescente.txt", n);
    if (d3 >= 0) {
        std::cout << "3. Decrescente:   " << d3 << " segundos (Pior caso)" << std::endl;
    }

    std::cout << "\n--- Testes concluidos ---" << std::endl;

    return 0;
}