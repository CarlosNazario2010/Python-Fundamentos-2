
# ANALISADOR DE MATRIZ:

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_terceira_coluna = maior_segunda_linha = 0

for l in range(0, 3):       

    for c in range(0, 3):    
        matriz[l][c] = int(input(f'DIGITE UM VALOR [{l}, {c}]: '))

for l in range(0, 3):   

    for c in range(0, 3):                                        # no print formatado a variavel matriz precisa dos indices l e c das listas 
        print(f'[{matriz[l][c]:^5}]', end='')                    # o :^5 centraliza o resultado em 5 espacos

        if matriz[l][c] % 2 == 0:                                # se o numero que passa pela matriz for par
            soma_pares += matriz[l][c]                           # o soma pares recebe ele mais o valor do indice lc da matriz 
   
    print('')                                                    # o print aqui quebra a linha apos o for das colunas, para gerar a linha        

print(f'A SOMA DOS VALORES PARES É: {soma_pares}')

for l in range(0, 3):                                            # para a linha no range ate 3 (pois sao 3 linhas na terceira coluna)
    soma_terceira_coluna += matriz[l][2]                         # pega e soma o terceiro elemento da coluna. Indice 2 de cada linha

print(f'A SOMA DOS VALORES DA TERCEIRA COLUNA É: {soma_terceira_coluna}')   

for c in range (0, 3):

    if matriz[1][c] > maior_segunda_linha:                            # matriz travada no indice 1 da linha (segunda linha)
        maior_segunda_linha = matriz[1][c]                            # se o novo numero for maior que o maior valor da 2* linha, este passa a ser o maior valor

print(f'O MAIOR VALOR DA SEGUNDA LINHA É: {maior_segunda_linha}')     