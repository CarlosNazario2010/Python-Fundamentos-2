# DIGITE 6 NUMEROS E SOME-OS SE ELES FOREM PARES:

print('DIGITE 6 NUMEROS E SOME-OS SE ELES FOREM PARES')

lista = []

for c in range(1, 7):                    
    num = int(input('DIGITE UM VALOR: '))

    if num % 2 == 0:
        lista.append(num)                    # ADICIONA A LISTA SE O NUMERO FOR PAR

soma = sum(lista)                            # SOMA A LISTA DE NUMEROS
print(f'A SOMA DOS NUMEROS PARES DIGITADOS É: {soma}')