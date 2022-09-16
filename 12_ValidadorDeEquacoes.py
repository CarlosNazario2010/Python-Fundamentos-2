# VERIFICADOR DE NUMEROS DE PARENTESES NA EQUACAO (VALIDADOR DE EQUACAO):

expressao = str(input('DIGITE UMA EXPRESSAO: '))

abre = []
fecha = []

for simb in expressao:

    if simb == '(':
        abre.append(simb)
    elif simb == ')':
        fecha.append(simb)

if len(abre) == len(fecha):
    print('SUA EXPRESSAO É VALIDA')
else:
    print('SUA EXPRESSAO NAO É VALIDA')
