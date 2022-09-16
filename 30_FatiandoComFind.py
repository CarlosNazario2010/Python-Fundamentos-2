url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

indice_interrogacao = url.find('?')             # METODO find() RETORNA O INDICE DO CARACTER
url_base = url[:indice_interrogacao]            # PASSADO COMO ARGUMENTO. RETORNA -1 CASO O 
print(url_base)                                 # A STRING NAO POSSUA O CARACTER
                                                
url_parametros = url[indice_interrogacao+1:]    # PARA URLS, CUJO COMPRIMENTO DA BASE
print(url_parametros)                           # E DOS PARAMENTROS VARIAM

