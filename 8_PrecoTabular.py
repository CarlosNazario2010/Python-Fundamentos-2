# TABELA DE PRECOS DE FORMA TABULAR (TUPLAS):

precos = ('LAPIS', 1.75, 'BORRACHA', 2, 'CADERNO', 15.9,
            'ESTOJO', 25, 'TRANSFERIDOR', 4.2, 'COMPASSO', 9.99,
                'MOCHILA', 120.32, 'CANETAS', 22.3, 'LIVRO', 50)

print(f'{"ITENS":->20} {"PRECO":->25}')
                                              # para a cada posicao entre o comeco e tamanho a listagem >>>
for pos in range(0, len(precos)):
    
    if pos % 2 == 0:                          # se a posicao for par vai pegar a lista com o nome dos itens
        print(f'{precos[pos]:.<35}', end='')  # exibe cada item alinhado a esquerda com 35 caracteres  
    else:                                   # e sem quebra de linha (que quebra após os preco)
        print(f'R$ {precos[pos]:>8.2f}')      # senao o impar pega o preco alinhado a direita