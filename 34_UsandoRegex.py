import re           # Regular Expression -- RegEx

                    # PADRAO = 5 dígitos + hífen (opcional) + 3 dígitos

endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca = padrao.search(endereco) 

if busca:                         # O '?' APOS O [-] INFORMA QUE O '-' É OPCIONAL
    cep = busca.group()
    print(cep)