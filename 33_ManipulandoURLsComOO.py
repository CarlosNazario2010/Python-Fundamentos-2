class ExtratorURL:

    def __init__(self, url):                     # INICA A CLASSE RETIRANDO CARACTERES ESPECIAIS
        self.url = self.sanitiza_url(url)        # COM O METODO strip(), E ANALIZANDO SE A URL
        self.valida_url()                        # ESTA PREENCHIDA

    def sanitiza_url(self, url):
      
        if type(url) == str:                  # SE O TYPE DA URL É STR    
            return url.strip()                  # APLICA O METODO strip()
        else:
            self.url = ''                       # SENAO RETORNA UMA STRING VAZIA         
                                                     
    def valida_url(self):       # SE A URL É FALSA, ISSO É, STRING VAZIA OU None LANCA O ERRO                     
        
        if not self.url:                       
            raise ValueError("A URL está vazia")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')       # PEGA A URL BASE - QUE VAI DO INICIO ATE 
        url_base = self.url[:indice_interrogacao]      # O CARACTER '?'
        return url_base
                                                       # PEGA OS PARAMETROS DA URL - QUE VAI DO
    def get_url_parametros(self):                      # INDICE DO CARACTER '?' ATE O FINAL
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

             # FUNCAO get_valor_parametro() RECEBE O PARAMETRO DA BUSCA
             # E, ATRAVES DA MANIPULACAO DOS INDICES, RETORNA O VALOR DA BUSCA


if __name__ == '__main__':

#  url = None or 0 or ''      # None, 0, '' retornam False
                              # ValueError: A URL está vazia
                 # None é uma classe propria do Python que nao possui o metodo strip()
                 # Ela retorna False, entao pode ser tratado pelo metodo valida_url() 

    url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar" 
    extrator_url = ExtratorURL(url)
  
    valor_quantidade = extrator_url.get_valor_parametro('quantidade')
    valor_moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
    valor_moeda_destino = extrator_url.get_valor_parametro('moedaDestino')

    print(f'QUANTIDADE:     {valor_quantidade}')
    print(f'MOEDA ORIGEM:   {valor_moeda_origem}')
    print(f'MOEDA DESTINO:  {valor_moeda_destino}')
  