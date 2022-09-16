# ANALISADOR DE DADOS DE VARIAS PESSOAS USANDO LISTAS E DICIONARIOS (C/ VALIDADOR DE DADOS:

c = 0                     # ESSE EXERCIO VALIDA OS DADOS DE SEXO E SE QUER CONTINUAR
total_idade = 0           # SE DIGITADO UM VALOR INVALIDO ELE PERMANECE NO LOOP ATE SER
mulheres = []             # DIGITADO UM DADO VALIDO
lista_pessoas = []

while True:
    nome = str(input('NOME: ')).upper()
    sexo = str(input('SEXO: '))
    
    while True:
        if sexo not in 'MmFf':
            sexo = str(input('ERRADO! RESPONDA APENAS [M/F]: '))
        if sexo in 'MmFf':
            break
    
    if sexo in 'Ff':
        mulheres.append(nome)
       
    idade = int(input('IDADE: '))
    pessoas = {'NOME': nome, 'SEXO': sexo, 'IDADE': idade}
    lista_pessoas.append(pessoas)
    c += 1
    total_idade += idade
    continuar = str(input('QUER CONTINUAR [S/N]: '))
        
    while True:
        if continuar not in 'SsNn':
            continuar = str(input('ERRADO! RESPONDA APEMAS [S/N]: '))
        else:
            break 
    if continuar in 'Nn':
        break

print('=-'*30 )

print(f'A) AO TODO TEMOS {c} PESSOAS CADASTRADAS')

media = float(total_idade / c)

print(f'B) A MÉDIA DE IDADE É DE {media:.2f} ANOS')
print(f'C) AS MULHERES CADASTRADAS FORAM {mulheres}')
print('D) AS PESSOAS COM IDADE SUPERIOR A MEDIA SAO:')

for p in lista_pessoas:
    if p['IDADE'] > media:
        print(f" --- {p['NOME']} COM {p['IDADE']} ANOS")