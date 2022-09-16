# ANALISADOR DE JOGADDOR COM DICIONARIOS DENTRO DE LISTAS:

time = []

while True:
    jogador = {}           # CUIDAR AS ASPAS SIMPLES E AS ASPAS DUPLAS
    partidas = []          # NUNCA USAR QUALQUER UMA DAS DUAS MAIS DE UMA VEZ
    jogador['NOME'] = str(input('NOME DO JOGADOR: ')).upper()
    total = int(input(f'QUANTAS PARTIDAS {jogador["NOME"]} JOGOU: '))
    
    for c in range(total):
        c += 1
        partidas.append(int(input(f'QUANTOS GOLS NA {c}° PARTIDA: ')))
    
    jogador['GOLS'] = partidas
    jogador['TOTAL'] = sum(partidas)
    time.append(jogador)

    continuar = str(input('QUER CONTINUAR [S/N]: '))
    
    if continuar in 'Nn':
        break

print('=-'*30)
print(f"{'COD'} {'NOME':>10} {'GOLS':>10} {'TOTAL':>10}")

for k, v in enumerate(time):    # SE FAZ O  FOR NOS KEYS E OS VALUES PARA IMPRIMIR O K, NO CASO O INDICE  
    print(f'{k:<10}', end='')      

    for d in v.values():  # SE FAZ O FOR NOS DADOS DOS VALUES PARA PARA PEGA-LOS A CADA LOOP
        print(f'{str(d):<12}', end='') # E MONTAR A TABELA
    print()

print('=-'*30)

while True:
    mostrar = int(input('DE QUAL JOGADOR VOCE QUER VER OS DADOS [999 P/ PARAR]: '))

    if mostrar == 999:
        print('<<<  PROGRAMA ENCERRADO  >>>')
        break

    if mostrar >= len(time):
        print('ERRO! NAO EXISTE ESSE JOGADOR. TENTE NOVAMENTE...')
        continue
    else:                                 #indice da lista time
        print(f'LEVANTAMENTO DO JOGADOR {time[mostrar]["NOME"]}')   #<< chave do dicionario jogador
        
        for i, g in enumerate(time[mostrar]['GOLS']):
                             #PARA INDICE E GOLS NA CHAVE GOLS DA LISTA TIME NO INDICE MOSTRAR  
            print(f'NO JOGO {i+1} O JOGADOR FEZ {time[mostrar]["GOLS"][i]}')
              # NA PARTIDA TAL O JOGADOR FEZ - INDICE I DA LISTA GOLS NO DICIONARIO DO JOGADOR
              # DO INDICE MOSTRAR DA LISTA TIME