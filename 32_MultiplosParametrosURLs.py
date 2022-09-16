url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

                                             # Separa base e parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
                      
                                             # Determina o parametro da busca = quantidade, no caso 
parametro_busca = 'moedaOrigem'

indice_parametro = url_parametros.find(parametro_busca)       # INDICE DE quantidade + MAIS O 
indice_valor = indice_parametro + len(parametro_busca) + 1    # TAMANHO DA quantidade + 1
indice_e_comercial = url_parametros.find('&', indice_valor)                 
     
         # O SEGUNDO PARAMETRO DO METODO find() DETERMINA APARTIR DE ONDE SERA BUSCADO O INDICE DE
         # PRIMEIRO ARGUMENTO. DO CONTRARIO, COMO A URL TEM UM '&' ANTES DO parametro_busca, ESTE 
         # PEGARIA O INDICE DA PRIMEIRA APARICAO DO '&' E O FATIAMENTO IRIA PARA TRAS
         # O QUE NAO FARIA SENTIDO E RETORNARIA UMA STRING VAZIA

                                                              # indice_e_comercial DETERMINA O FIM
if indice_e_comercial == -1:                                  # DO FATIAMENTO, VISTO QUE APARTIR DELE
    valor = url_parametros[indice_valor:]                     # UM NOVO PARAMETRO COMECA
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

                   # SE NAO HOUVER MAIS '&' VAI ATE O FINAL, POIS NAO HA MAIS PARAMETROS NA URL
                   # SENAO VAI DO INDICE DO VALOR DO PARAMETRO ATE O COMECO DO PROXIMO PARAMETRO

print(url_parametros)
print(parametro_busca)
print(valor)
print('')

print(indice_parametro)
print(indice_valor)
print(indice_e_comercial)        # obs - indice_e_comercial APARTIR DO indice_valor
