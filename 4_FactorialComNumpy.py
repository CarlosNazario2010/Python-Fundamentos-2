# FATORIAL COM WHILE E O PACOTE NUMPY:

import numpy as np

num = int(input('DIGITE UM NUMERO PARA CALCULAR O SEU FATORIAL: '))
x = num
lista = [num]

while x > 1:
    fat = num - 1
    num = fat
    lista.append(num)            # A LISTA RECEBE O NUMERO SEMPRE DIMINUIDO DE 1 A CADA LOOP
    x -= 1 

print(f'O FATORIAL DO NUMERO É A MULTIPLICACAO DE: {lista}', end=' ')
print(f' = {np.prod(lista)}')     
                                # O NUMPY.PROD MULTIPLICA OS ITENS DA LISTA QUE É O FATORIAL