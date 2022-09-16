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
    numero = input('NUMERO: ')

    for caracter in numero:
        contador = 0

        try:
            
            for digito in Digitos[int(caracter)]:
                print(digito.replace('*', str(numero[int(caracter) - 1])))
                contador += 1
            
                if contador == 7:
                    print('')
                    contador = 0
        
        except ValueError as err:
            print(err)
            continue

except ValueError as err:
    print(err)

