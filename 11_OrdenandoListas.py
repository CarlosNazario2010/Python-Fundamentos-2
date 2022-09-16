# ORDENANDO VALORES E INDICANDO O INDICE ATUAL (LISTAS):

lista = []

for i in range(5):
    valor = int(input('DIGITE UM VALOR: '))
    lista.append(valor)                       # O LISTA.INDEX(VALOR) RETORNA A POSICAO DO EM QUE O VALOR FOI
    lista.sort()                              # INSERIDO, SEMPRE ATUALIZADO PELO SORT (EM ORDEM CRESCENTE)
    print(f'O VALOR {valor} FOI ADICIONADO A POSICAO {lista.index(valor)} DA LISTA')

print(f'OS VALORES DA LISTA SAO: {lista}')