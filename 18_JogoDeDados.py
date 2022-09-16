#  JOGO DE DADOS COM QUATRO JOGADORES:

from random import randint
from time import sleep
from operator import itemgetter 

jogo = {'JOGADOR 1': randint(1,6),
        'JOGADOR 2': randint(1,6),                     # OS VALUES DO DICIONARIO SAO OS RANDINT DE 1 A DO DADO
        'JOGADOR 3': randint(1,6),
        'JOGADOR 4': randint(1,6)}

ranking = {}
print('=== VALORES SORTEADOS ===')

for k, v in jogo.items():
    sleep(1)
    print(f'O {k} TIROU {v} NO DADO')

ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True)

sleep(1.5)                                                 # SORTED ORDENA O DICIONARIO, O KEY = ITEMGETTER ORDENA PELOS VALUES (1) DO DICIONARIO
print(f'    ===  RANKING ===')                             # E REVERSE É PARA PEGAR OS NUMEROS SORTEADOS EM ORDEM DECRESCENTE

for c, pos in enumerate(ranking):                                               
    sleep(1)                                                # PARA CONTADOR E POSICAO NO RANKING ENUMERADO
    print(f'O {pos[0]} FICOU NA {c+1}* POSICAO')            # O JOGADOR (ITEM 0 DO DO DICIONARIO RANKING,
                                                            # QUE É O DICIONARIO JOGO ODENADO PELO LANCE JOGADO (RANDINT, O INTEMGETTER 1, O VALUES)