# LISTA DE FORMA ORDENADA E ELIMINADO NUMEROS DIGITADOS REPETIDOS:

lista = []
continuar = ''

while True:
    valor = int(input('DIGITE UM VALOR: '))
    contunuar = str(input('DESEJA CONTINUAR [S/N]:')).upper()
    
    if valor not in lista:
        lista.append(valor)
    
    if continuar == 'S':
        continue
    elif contunuar == 'N':
        break

lista.sort()   # COLOCA OS NUMEROS EM ORDEM CRESCENTE. NAO COLOCAR DENTRO DE UMA VARIAVEL
print(f'OS NUMEROS DIGITADOS FORAM: {lista}')