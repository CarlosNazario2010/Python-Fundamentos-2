# MONTANDO UMA MATRIZ 3 x 3:

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]                          # matriz comeca vazia (uma lista dentro de outra)

for l in range(0, 3):                                               # preenche a linha de 0 a 2
   
    for c in range(0, 3):                                           # preenche a coluna de 0 a 2
        matriz[l][c] = int(input(f'DIGITE UM VALOR [{l}, {c}]: '))  # COMECA NA COLUNA 1 LINHA 1, COLUNA 2, LINHA 1 

for l in range(0, 3):                                               # mesmo loop anterior                               # COLUNA 3, LINHA 1, COLUNA 1, LINHA 2, ETC...

    for c in range(0, 3):                                           # agora para exibir a matriz
        print(f'[{matriz[l][c]:^5}]', end='')                                                            # EXIBE NO LOOP O PRIMEIRO ITEM DA COLUNA NA LINHA, DEPOIS O SEGUNDO DA COLUNA, ETC..
                                                                    # o end='' impede a quebra de linha (tudo na mesma linha)
    print('')                                                       # o print vazio quebra a linha para cada linha (apos os 3 loops das colunas)
