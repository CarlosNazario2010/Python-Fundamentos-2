# SEQUENCIA DE FIBONACCI:

termo = int(input('QUANTOS TERMOS DA SEQUENCIA DE FIBONACCI VOCE QUER MOSTRAR: '))

n1 = 0
n2 = 1
quant = termo - 2                               # QUANTIDADE MOSTRADA MENOS OS DOIS PRIMEIROS TERMOS CONSTANTES

print(f'{n1} > {n2}', end=' > ')                # SEQUENCIA COMECA COM OS TERMOS CONSTANTES 0 E 1

while quant > 0:                                # ENQUANTO A QUANTIDADE SOLICITADA MENOS OS DOIS PRIMEIROS TERMOS
    quant -= 1                                  # CONSTATES MAIOR QUE ZERO, ESTA É INCREMENTADA MAIS UMA UNIDADE
    n3 = n1 + n2                                # SOMA OS TERMOS ANTERIORES
    print(n3, end='')                           # EXIBE O TERMO SOMADO SEM QUEBRA DE LINHA
    print(' > ' if quant > 0 else ' > FIM ', end=' ')          # CONDICIONA O SINAL SE ULTIMO TERMO
    n1 = n2                                     # APOS A EXIBICAO DO TERMO SOMADO, O NOVO PRIMEIRO TERMO VAI RECEBER O SEGUNDO
    n2 = n3                                     # TERMO DA SOMA E O NOVO SEGUNDO TERMO RECEBE O TERMO DA SOMA