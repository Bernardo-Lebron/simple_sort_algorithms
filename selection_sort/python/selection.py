import time
import os
import sys

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# --- Configuração do N vindo do Makefile ---
# Se houver um argumento, converte para int. Se não, usa 1000.
num_linhas = int(sys.argv[1]) if len(sys.argv) > 1 else 1000

# --- Configuração do Caminho ---
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "..", "dados", "aleatorio.txt")

try:
    with open(file_path, "r") as f:
        # Lê exatamente 'num_linhas' do arquivo
        data = []
        for _ in range(num_linhas):
            linha = f.readline()
            if not linha:
                break
            data.append(float(linha.strip()))

    start = time.time()
    selection_sort(data)
    end = time.time()

    # Saída formatada para o benchmark
    print(f"Tempo: {end - start:.6f} s")
    if data:
        print(f"Menor valor: {data[0]}")

except FileNotFoundError:
    print(f"Erro: O arquivo nao foi encontrado em: {file_path}")
except Exception as e:
    print(f"Ocorreu um erro em python/selection.py: {e}")