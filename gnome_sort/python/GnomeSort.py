
import sys
import time
 
def gnome_sort(arr):
    i = 0
    while i < len(arr):
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr
 
if len(sys.argv) < 2:
    print("Uso: python3 gnome.py <arquivo.txt>")
    sys.exit(1)
 
with open(sys.argv[1], 'r') as f:
    arr = [int(line.strip()) for line in f if line.strip()]
 
start = time.perf_counter()
 
gnome_sort(arr)
 
ms = (time.perf_counter() - start) * 1000
 
print(f"  n={len(arr):<8}  tempo: {ms:.4f} ms")
