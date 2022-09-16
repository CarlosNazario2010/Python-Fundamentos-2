# ANALISE DE DADOS DE UMA JOGADOR USANDO DICIONARIOS:

jog = str(input('NOME DO JOGADOR: ')).upper()
part = int(input('NUMERO DE PARTIDAS: '))
c = 0
total = 0

for gols in range(part):
    c += 1
    gols = int(input(f'QUANTOS GOLS NA {c}* PARTIDA: '))
    total += gols

ficha = {'NOME' : jog, 'TOTAL DE PARTIDAS': c, 'TOTAL DE GOLS': total}
print('=-'*35)

for k, v in ficha.items():
    print(f'O CAMPO {k} TEM O VALOR: {v}')