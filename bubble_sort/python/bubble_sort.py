import sys
import time

def bubble_sort(nums):
    """
    Bubble Sort O(n^2)
    Implementação in-place com otimização de parada antecipada.
    """
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break  # Melhor caso: O(n)

def rodar_teste(nome_arquivo, n):
    try:
        # Lê o arquivo e converte para lista de floats
        with open(nome_arquivo, 'r') as f:
            # Carrega apenas as primeiras 'n' linhas
            v = []
            for _ in range(n):
                line = f.readline()
                if not line:
                    break
                v.append(float(line.strip()))

        if len(v) < n:
            print(f"Aviso: O arquivo {nome_arquivo} possui apenas {len(v)} registros.")

        # Medição de tempo usando time.perf_counter() (alta precisão no Linux)
        start = time.perf_counter()
        bubble_sort(v)
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
    print(f"--- Iniciando Benchmark Python (N: {n}) ---\n")

    testes = [
        ("Crescente", "crescente.txt", "(Melhor caso)"),
        ("Aleatorio", "aleatorio.txt", "(Caso Médio)"),
        ("Decrescente", "decrescente.txt", "(Pior caso)")
    ]

    for nome, path, desc in testes:
        tempo = rodar_teste(path, n)
        if tempo >= 0:
            print(f"{testes.index((nome, path, desc)) + 1}. {nome:12}: {tempo:.6f} segundos {desc}")

    print("\n--- Testes concluidos ---")

if __name__ == "__main__":
    main()