total = 0
contador = 0

print('Digite um numero ou CTRL d PARA SAIR')

while True:
  
  try:
    numero = input(f'Numero: ')
    
    if numero:
      
      try:                                  # OBS - PODERIA SER USADO SOMENTE UM TRY E DUAS EXCESSOES
        numero = int(numero)                # MAS É UMA BOA PRATICA AGRUPAR AS EXCESSOES
        total += numero
        contador += 1
      except ValueError as err:
        print(err)
        continue
  
  except EOFError:
    break

if contador:
  print('contador = ', contador, 'total = ', total, 'media = ', total/contador)

