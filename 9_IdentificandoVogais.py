# IDENTIFIQUE QUAIS SAO AS VOGAIS DAS PALAVRAS:

palavras = ('APRENDER', 'PROGRAMAR', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
            'PRATICAR', 'TRABAHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

                                                                # PERCORRE A PALAVRA NA TUPLA PALAVRAS
for palavra in palavras:                                        # O \n QUEBRA A LINHA NO INICIO DE CADA LOOP FOR
    print(f'\nNA PALAVRA {palavra.lower()}, TEMOS: ', end='')   # O end= '' IMPEDE QUEBRA DE LINHA
    
    for letra in palavra:                                       # PERCORRE AS LETRAS NA PALAVRA QUE É UMA LISTA DE LETRAS
       
        if letra.upper() in 'AEIOU':                            # SE LETRA FOR VOGAL, EXIBE A LETRA SEM A QUEBRA DE LINHA
            print(f'{letra}', end='')