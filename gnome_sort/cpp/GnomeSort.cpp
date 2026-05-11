#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>

void gnome_sort(std::vector<int>& arr) {
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

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Uso: " << argv[0] << " <arquivo.txt>\n";
        return 1;
    }
    std::ifstream f(argv[1]);
    if (!f.is_open()) {
        std::cerr << "Erro ao abrir arquivo: " << argv[1] << "\n";
        return 1;
    }
    std::vector<int> arr;
    int x;
    while (f >> x) arr.push_back(x);
    f.close();
    auto start = std::chrono::high_resolution_clock::now();
    gnome_sort(arr);
    auto end = std::chrono::high_resolution_clock::now();
    double ms = std::chrono::duration<double, std::milli>(end - start).count();
    std::cout << "  n=" << arr.size() << "\t  tempo: " << ms << " ms\n";
    return 0;
}
