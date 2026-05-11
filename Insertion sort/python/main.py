import time

def insertion_sort(arr):

    for i in range(1, len(arr)):

        chave = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = chave



limite = 100000



numeros = []

with open("C:\\Users\\Arthur\\Desktop\\AEDS TRAB 2\\aleatorio.txt") as file:

    for i, linha in enumerate(file):

        if i >= limite:
            break

        numeros.append(int(linha.strip()))




start = time.perf_counter()

insertion_sort(numeros)

end = time.perf_counter()

print("Tempo:", round(end - start, 6), "segundos")