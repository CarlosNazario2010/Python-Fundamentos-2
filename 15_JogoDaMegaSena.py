# JOGO DA MEGA SENA (PREENCHEDOR AUTOMATICO DE JOGOS)

import time
import random

print('=======  JOGO DA MEGA SENA  ======')

jogos = int(input('QUANTOS JOGOS VOCE QUER JOGAR: '))
num = 0

for jogos in range(0, jogos):
    time.sleep(1)
    print(f'JOGO: {jogos + 1}  :-->>  ', end= '')
    lista_jogo = []
    contador = 0

    while contador < 6:
        num = random.randint(1, 60)

        if num not in lista_jogo:
            lista_jogo.append(num)
            contador += 1
            print(f'{num:^4}', end='')

    print('')

print('=====  BOA SORTE =====')