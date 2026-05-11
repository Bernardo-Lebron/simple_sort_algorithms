import sys
import time
import os

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def rodar_teste(nome_arquivo, n):
    try:
        with open(nome_arquivo, 'r') as f:
            v = []
            for _ in range(n):
                line = f.readline()
                if not line:
                    break
                v.append(float(line.strip()))

        if len(v) < n:
            print(f"Aviso: O arquivo {nome_arquivo} possui apenas {len(v)} registros.")

        start = time.perf_counter()
        selection_sort(v)
        end = time.perf_counter()

        return end - start
    except FileNotFoundError:
        print(f"Erro: Arquivo {nome_arquivo} não encontrado.")
        return -1
    except Exception as e:
        print(f"Erro: {e}")
        return -1

def main():
    if len(sys.argv) < 2:
        print(f"Uso: python3 {sys.argv[0]} <n_elementos>")
        sys.exit(1)

    n = int(sys.argv[1])
    base_path = os.path.dirname(__file__)

    print(f"--- Iniciando Benchmark Python (N: {n}) ---\n")

    testes = [
        ("Crescente",   os.path.join(base_path, "..", "dados", "crescente.txt"),   "(Melhor caso)"),
        ("Aleatorio",   os.path.join(base_path, "..", "dados", "aleatorio.txt"),   "(Caso Médio)"),
        ("Decrescente", os.path.join(base_path, "..", "dados", "decrescente.txt"), "(Pior caso)"),
    ]

    for i, (nome, path, desc) in enumerate(testes):
        tempo = rodar_teste(path, n)
        if tempo >= 0:
            print(f"{i + 1}. {nome:12}: {tempo:.6f} segundos {desc}")

    print("\n--- Testes concluidos ---")

if __name__ == "__main__":
    main()