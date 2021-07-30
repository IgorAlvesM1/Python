import random

valAle=[]
valAle2=[]

for i in range(50):
  valAle.append(int(random.uniform(0,50)))

  valAle2.append(int(random.uniform(0,50)))

ordenada=sorted(valAle+valAle2)
print(valAle)
print(valAle2)
print(ordenada)
print(len(ordenada))