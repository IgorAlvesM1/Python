import random
import statistics
listaAle= []
for i in range(100):
  listaAle.append(round(float(random.uniform(0, 200))))
print(listaAle)
with open('Numeros.txt',mode='w+') as arquivo:
  arquivo.write(str(listaAle))

print(statistics.mean(listaAle))
print(statistics.variance(listaAle))
print(statistics.stdev(listaAle))