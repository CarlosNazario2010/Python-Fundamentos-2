import re  

# re.compile() - COMPILA O PADRAO CRIADO
# re.search()  - extrai o valor que esteja de acordo com o padrão fornecido
# re.match()   - verifica se o texto está de acordo com o padrão
# re.group()   - AGRUPA E RETORNA O PADRAO DE UM search() OU UM match()


endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"
         
                    # PADRAO = 5 dígitos + hífen (opcional) + 3 dígitos

padrao = re.compile("[0-9]{5}[-]{0,3}[0-9]{3}")
busca = padrao.search(endereco) 
if busca:                          # O HIFEM ENTRE OS PARENTESES DETERMINA O INTERVALO DA BUSCA
    cep = busca.group()            # DE 0 A 9 NO CASO
    print(cep)                     
                                   # ENTRE AS CHAVES PODEM SER PASSA A QUANTIDADE DE VEZES QUE SE
                                   # QUE QUE O PADRAO SE REPITA, 5 VEZES E 3 VEZES

                                   # OU PODE SER PASSADA NAS CHAVES, SEPARADAS PELA VIRGULA, UM  
                                   # INTERVALO DE QUANTIDADES, DE 0 A 3 NO CASO