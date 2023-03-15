
import random
import time

def bruteForceSiralama(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

arr = [random.randint(1, 100000) for i in range(10000)]

baslangic = time.time()
bruteForceSiralama(arr)
bitis = time.time()

print("Sıralanmış dizi: ", arr)
print("Sıralama işlemi süresi: ", bitis - baslangic, " saniye")
