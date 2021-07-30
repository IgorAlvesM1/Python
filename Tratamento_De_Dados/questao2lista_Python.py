segundos=input('Coloque a quantidade de segundos: ')

if(segundos.isnumeric())==False:
 print ('Dado invalido')

else:
  ttl_seg=int(segundos)
  horas=ttl_seg//3600
  segRestantes=ttl_seg %3600 
  minutos=segRestantes//60
  restSegundos=segRestantes%60

  print('Essa quantidade de segundos é igual a: '+str(horas)+' horas '+str(minutos)+' minutos '+str(restSegundos)+' segundos')

  print(str(horas)+(':')+str(minutos)+(':')+str(restSegundos))