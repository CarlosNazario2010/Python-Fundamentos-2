# CADASTRO DE EMPREGADOS USANDO DICIONARIOS:

while True:
    nome = str(input('NOME: ')).upper()
    nasc = int(input('ANO DE NASCIMENTO: '))
    cart = int(input('CARTEIRA DE TRABALHO (0 SE NAO TEM): '))
    idade = f'{2021 - nasc} ANOS'
    cad = {'NOME' : nome, 'IDADE' : idade, 'CTPS': cart}
  
    if cart == 0:
        print('=-'*30)
        for k, v in cad.items():
            print(f' --- {k} TEM O VALOR >> {v}')
        break
    else:
        cont = int(input('ANO DE CONTRATACAO: '))
        sal = float(input('SALARIO: '))
        apos = cont + 35 
        cad['ANO DE CONTRATACAO'] = cont                 # AS [] ADICIONA A CHAVE NO DICIONARIO E O = RECEBE O VALOR
        cad['SALARIO'] = f'R$ {sal:.2f}'
        cad['ANO DE APOSENTADORIA (65 ANOS)'] = f'{apos}'
        print('=-'*30)
    
    for k, v in cad.items():
        print(f' --- {k} TEM O VALOR >> {v}')
    break
