url = "bytebank.com/cambio?moedaDestino=dolarmoedaOrigem=real"

indice_interrogacao = url.find('?')

print(indice_interrogacao)

url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]

print(url_parametros)                                         # SE AO INVES DE UM CARACTER, FOR PASSADO UMA STRING
                                                              # PARA O METODO find(), ESTE RETORNARA O INDICE DO
parametro_busca = 'moedaOrigem'                               # PRIMEIRO CARACTER DA STRING 
indice_parametro = url_parametros.find(parametro_busca)

print(indice_parametro)

indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:]

print(valor)                                        # INDICE DO VALOR = INDICE DE moedaOrigem + MAIS O PROPRIO moedaOrigem + 1
