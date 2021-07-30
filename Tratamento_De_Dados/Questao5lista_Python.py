ext=['zero','um', 'dois' , 'tres' , 'quatro' , 'cinco' ,'seis', 'sete', 'oito' , 'nove']
numeral=input('Digite os numeros:')
try:
  val=int(numeral)
 
except:
  print('Digite numeros inteiros')
a=list(map(int,numeral))

for i in range(len(ext)):
   valor= a[i]
   print(ext[valor])
