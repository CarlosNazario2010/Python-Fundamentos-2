# DIGITE A SOMA E QUANTIDADE DE TODOS OS NUMEROS IMPARES MENORES QUE 500 E MULTIPLOS DE 3:

lista = []    # lista vazia        
c = 0      

for x in range(1, 500, 2):
    
    if x % 3 == 0 :         # pega os multiplo de 3. O % retorna os valores divisiveis por 3 c/ resto 0 
        lista.append(x)     # adiciona na lista cada número passado pelo loop for
        c += 1              # contador recebe sempre uma unidade a cada loop

soma = sum(lista)           # soma os valores de uma lista
print(f'A SOMA DE TODOS OS IMPARES MENORES DE 500 E MULTIPLOS DE 3 É: {soma}')
print(f'SAO {c} NUMEROS SOMADOS')