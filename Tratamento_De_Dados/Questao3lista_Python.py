import random

numeros = []

for i in range(100):
    numeros.append(round(float(random.uniform(0.000, 100.000)),3))
incremental = sorted(numeros)
decremental = list(reversed(incremental))
print("incremental" and incremental)
print("decremental" and decremental)
