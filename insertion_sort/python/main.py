import sys
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

def rodar_teste(arquivo, n):
    try:
        with open(arquivo) as f:
            numeros = []
            for i, linha in enumerate(f):
                if i >= n:
                    break
                numeros.append(int(linha.strip()))
        start = time.perf_counter()
        insertion_sort(numeros)
        return time.perf_counter() - start
    except Exception:
        return None

if len(sys.argv) < 2:
    print("Uso: python3 main.py <n_elementos>")
    sys.exit(1)

n = int(sys.argv[1])
print(f"--- Iniciando Benchmark Insertion Sort (N: {n}) ---\n")

t1 = rodar_teste("crescente.txt", n)
if t1 is not None:
    print(f"1. Crescente:   {t1:.6f} segundos (Melhor caso)")

t2 = rodar_teste("aleatorio.txt", n)
if t2 is not None:
    print(f"2. Aleatorio:   {t2:.6f} segundos (Caso Medio)")

t3 = rodar_teste("decrescente.txt", n)
if t3 is not None:
    print(f"3. Decrescente: {t3:.6f} segundos (Pior caso)")

print("\n--- Testes concluidos ---")