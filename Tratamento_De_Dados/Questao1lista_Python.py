try:
  nota1=float(input('Insira a primeira nota:'))
  nota2=float(input('Insira a segunda nota:'))
 
  faltas=float(input('Insira a quantidade de faltas:'))

except:
  print('Dados inválidos, insira uma nota entre 0 e 10')

while True:
  if nota1>10:
    print('Erro:Você inseriu uma nota no primeiro campo maior que 10')
    break
  if nota2>10:
    print('Erro:Você inseriu uma nota no segundo campo maior que 10')
    break
    
  if faltas>22.5:
   print('Reprovado por faltas')
   break
  media=(nota1+nota2)/2
  if media>=9:
   print('Aprovado com SS')
   print('Média:',media)
   break
  elif media>=7:
    print('Aprovado com MS')
    print('Média:',media)
    break
  elif media>=5:
   print('Aprovado com MM')
   print('Média:',media)
   break
  elif media>=3:
   print('Reprovado com MI')
   print('Média:',media)
   break
  elif media>=1:
   print('Reprovado com II')
   print('Média:',media)
   break
  elif media>=0:
   print('Reprovado com SR')
   print('Média:',media)
   break
 
