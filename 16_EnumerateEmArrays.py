# ANALIZADOR DE NOTAS UTILIZANDO LISTAS (INDICES AO INVES DE CHAVES):

ficha = []
continuar = ''

while True:
    nome = str(input('NOME: ')).upper()
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])            # FICHA ALIMENTADA COM UMA LISTA COMPOSTA COM NOME(0), NOTAS(1)
    continuar = str(input('QUER CONTINUAR [S/N]: '))       # COM DUAS VARIAVEIS (NOTA1 E NOTA2) E MEDIA(2)          
   
    if continuar in 'Nn':
        break

print('='*30)
print(f'{"No.":<8} {"NOME":<10} {"MEDIA":>8}')            # PRINT FORMATADO COM ALINHAMENTO A ESQUERDA E DIREITA
print('='*30)

for i, aluno in enumerate(ficha):                         # PARA O INDICE E O ALUNO NA FICHA (INFORMA DUAS VARIAVEIS)
    print(f'{i:<8} {aluno[0]:<10} {aluno[2]:>8.1f}')      # EXIBE O INDICE, O NOME DO ALUNO (INDICE 0 DA LISTA FICHA)

while True:                                               # E EXIBE A MEDIA (INDICE 2 DA LISTA FICHA), TODOS FORMATADOS
    print('='*35)                                                                                   # E ALINHADOS
    opcao = int(input('MOSTRAR AS NOTAS DE QUAL ALUNO: (999 P/ INTERROMPER): '))
    
    if opcao == 999:                                            # VARIAVEL OPCAO NO CASO RECEBE O INDICE DO ALUNO
        print('FINALIZANDO...')
        break
    
    if opcao <= len(ficha) - 1:                                  # SE A OPCAO FOR MENOR QUE A QUANTIDADE DE ALUNOS
        print(f'NOTAS DE {ficha[opcao][0]} SAO {ficha[opcao][1]}') 
                                                               # EXIBE A LISTA DOS DADOS DE CADA ALUNO (INDICE OPCAO DA LISTA FICHA)
                                                               # E PARA CADA ALUNO PEGA O NOME (INDICE 0 DA LISTA FICHA) E AS NOTAS (INDICE 1 DA LISTA FICHA)