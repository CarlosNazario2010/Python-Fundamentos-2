
zero =   ['  ***  ', ' *   * ', ' *   * ', ' *   * ', ' *   * ', ' *   * ', '  ***  ']
um =     ['   *   ', '  **   ', '   *   ', '   *   ', '   *   ', '   *   ', '  ***  ']
dois =   ['  ***  ', ' *   * ', ' *  *  ', '   *   ', '  *    ', ' *     ', ' ***** ']
tres =   ['  ***  ', ' *   * ', '     * ', '    *  ', '     * ', ' *   * ', '  ***  ']
quatro = ['    *  ', '   **  ', '  * *  ', ' *  *  ', ' ******', '    *  ', '    *  ']
cinco =  [' ***** ', ' *     ', ' *     ', ' ****  ', '     * ', ' *   * ', '  ***  '] 
seis =   ['  ***  ', ' *     ', ' *     ', ' * **  ', ' *   * ', ' *   * ', '  ***  ']
sete =   [' ***** ', '     * ', '    *  ', '   *   ', '  *    ', '  *    ', '  *    ']
oito =   ['  ***  ', ' *   * ', ' *   * ', '  ***  ', ' *   * ', ' *   * ', '  ***  ']
nove =   ['  **** ', ' *   * ', ' *   * ', '  **** ', '     * ', '     * ', '     * ']

Digitos = [zero, um, dois, tres, quatro, cinco, seis, sete, oito, nove]

try:
    digitos = input('Digite um numero: ')
    print()
    linha = 0

    while linha < 7:
        coluna = 0 
        line = ''

        while coluna < len(digitos):
            numero = int(digitos[coluna])
            digito = Digitos[numero]  
            line += digito[linha].replace('*', str(numero))
            coluna += 1
      
        print(line)
        linha += 1

except ValueError as err:
    print(err, 'em', digitos)
