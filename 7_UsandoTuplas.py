# CLASSIFICACAO DO BRASILEIRAO (TRABALHANDO TUPLAS)

print('==== TABELA DO BRASILEIRAO ====')

times = ('FLAMENGO', 'INTERNACIONAL', 'ATLETIOCO MINEIRO', 'SAO PAULO',
            'FLUMINENSE', 'GREMIO', 'PALMEIRAS', 'SANTOS',
                'ATLETICO PARANAENSE', 'BRAGANTINO', 'CEARA', 'CORINTHIANS',
                    'ATLETICO GOIANIENSE', 'BAHIA', 'SPORT', 'FORTALEZA',
                        'VASCO', 'GOIAS', 'CORITIBA', 'BOTAFOGO')

print(times)

print('')

print(f'OS CINCO PRIMREIROS COLOCADOS SAO: {times[:5]}')
print(f'OS QUATRO ULTIMOS COLOCADOS SAO: {times[16:]}')
print(f'OS TIMES EM ORDEM ALFABETICA SAO: {sorted(times)}')
print(f'O SANTOS ESTA NA {times.index("SANTOS")+1} POSICAO')

# O SANTOS DENTRO DO INDEX NECESSARIAMENTE PRECISA DE ASPAS DUPLAS, PARA NAO SER 
# CONFUNDIDA COM A ASPAS SIMPLES DO PRINT FORMATADO