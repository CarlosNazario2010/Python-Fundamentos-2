#  APORTE DE UM LOTE A CADA QUEDA DE 10% E UM APORTE COM O DOBRO DO VALOR APORTADO COM UMA QUEDA DE 50%

print('')

preco = float(input('        DIGITE O PRECO DA AÇÃO: R$ '))
soma_lote = []
quantidade = int(100)
queda = 0
cont = 0

print('')

for c in range(0, 6): 
    lote = preco * quantidade
    c += 1
    
    if c <= 1:
        print(f'R$ {lote:,.2f} gastos no {c}* lote ao preço de compra de R$ {preco:.2f}')
        print('')
    else:
        queda += 10
        print(f'R$ {lote:,.2f} gastos no {c}* lote c/ {queda} % de queda ao preço de compra de R$ {preco:.2f}')
    
    preco_queda = preco* 0.9  
    preco = preco_queda
    soma_lote.append(lote)

print(' ')
valores = []

for x in soma_lote:
    x = valores. append(float(x))

soma_valores = sum(valores)
total_acoes = c * quantidade
print(f'FOI GASTO R$ {soma_valores:,.2f} NA COMPRA DE {total_acoes:.0f} AÇOES')

preco_medio = soma_valores / (total_acoes)
print(f'PRECO MEDIO DE R$ {preco_medio:.2f}')
print(f'O PRECO DE MERCADO NO DIA DO APORTE DOBRADO (queda de 60%) É DE {preco:.2f}')

print('')
prejuizo_atual = 1 - (preco / preco_medio)
print(f'O PREJUIZO ATUAL É DE {prejuizo_atual:.2%} COM UMA QUEDA DE 60% DO PRECO INICIAL')

novo_aporte = soma_valores*2
nova_quantidade = int(soma_valores / preco)
novo_total_acoes = total_acoes + nova_quantidade
preco_medio_total = novo_aporte / novo_total_acoes

print(f'''
          COM UM APORTE DE O DOBRO DO VALOR APÓS A QUEDA DE 60% 

          O NOVO VALOR DO TOTAL APORTADO É DE R$ {novo_aporte:,.2f}

          COM A QUANTIDADE DE {novo_total_acoes} ACOES 

          A UM NOVO PRECO MEDIO DE R$ {preco_medio_total:.2f}
''')

prejuizo = 1 - (preco / preco_medio_total)

print(f'''O PREJUIZO É DE 60 % SE NAO FOR FEITO MAIS APORTES DESDE PRIMEIRA COMPRA.

PREJUIZO DE {prejuizo_atual:.2%}, CASO NAO FOSSE FEITO O APORTE DO DOBRO DO VALOR.

PREJUIZO DE {prejuizo:.2%} SE FOR FEITO O APORTE NO DOBRO DO VALOR INVESTIDO.

PRECO MEDIO É DE R$ {preco_medio_total:.2f} E O PRECO ATUAL DE MERCADO É R$ {preco:.2f}

É NECESSARIO QUE A ACAO SE VALORIZE R$ {preco_medio_total - preco:.2f} PARA QUE SE ZERE O PREJUIZO

O GANHO OU PERDA PARA CADA CENTAVO VARIADO E COM ESSA QUANTIDADE DE ACOES É R$ {novo_total_acoes*0.01:.2f}
''')