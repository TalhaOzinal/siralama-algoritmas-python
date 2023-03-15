
import random
import time

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    sol = []
    sag = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            sol.append(arr[i])
        else:
            sag.append(arr[i])

    return quickSort(sol) + [pivot] + quickSort(sag)

arr = [random.randint(1, 100000) for i in range(10000)]

baslangic = time.time()
siralanmis = quickSort(arr)
bitis = time.time()

print("Sıralanmış: ", siralanmis)
print("Süre: ", bitis - baslangic, " saniye")
