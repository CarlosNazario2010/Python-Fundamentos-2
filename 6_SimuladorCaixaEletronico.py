# SIMULADOR DE CAIXA ELETRONICO

from math import trunc

print('=== BANCO TESTE ===')

saque = float(input('DIGITE O VALOR DO SAQUE R$: '))

while saque >= 100:                        # enquanto o saque for maior que 100
    cem = trunc(saque/100)                 # trunc pega o valor inteiro (da o numero de notas)
    print(f'{cem} NOTAS DE 100 REAIS')     # exibe a quantidade de notas
    saque = saque - (cem*100)              # atualiza o saque (valor menos as notas de 100)

while saque < 100 and saque >= 50:      
    cinquenta = trunc(saque/50)                   # os loops a seguir repetem a sequencia 
    print(f'{cinquenta} NOTAS DE 50 REAIS')       # realizada nas notas de 100 para as outras
    saque = saque - (cinquenta*50)

while saque < 50 and saque >= 20:
    vinte = trunc(saque/20)
    print(f'{vinte} NOTAS DE 20 REAIS')
    saque = saque - (vinte*20)

while saque < 20 and saque >= 10:
    dez = trunc(saque/10)
    print(f'{dez} NOTAS DE 10 REAIS')
    saque = saque - (dez*10)

while saque < 10 and saque >= 5:
    cinco = trunc(saque/5)
    print(f'{cinco} NOTAS DE 5 REAIS')
    saque = saque - (cinco*5)

while saque < 5 and saque >= 2:
    dois = trunc(saque/2)
    print(f'{dois} NOTAS DE 2 REAIS')
    saque = saque - (dois*2)

if saque > 0:                     # no final se retiradas todas as notas maiores que 2, exibe
    print(f'MAIS R$ {saque}')     # o resto do saque (menor que R$ 2.00) 