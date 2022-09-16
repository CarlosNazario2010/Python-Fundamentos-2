import re

class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
       
        if type(url) == str:
            return url.strip()      # OBS - NOS REGEX [] INDICAM QUE PODE SER QUALQUER UM DOS VALORES
        else:                       # () INDICAM QUE DEVE SER EXATAMENTE AQUELES CARACTERES
            return ""

    def valida_url(self):
        
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        
        if not match:
            raise ValueError("A URL não é válida.")       # PASSA O PADRAO DA URL
                                                          # (http(s)?://)? - OPCIONAL    
    def get_url_base(self):                               # (s)? - OPCIONAL
        indice_interrogacao = self.url.find('?')          # (www.)? - OPCIONAL
        url_base = self.url[:indice_interrogacao]         # bytebank.com - FIXO
        return url_base                                   # (.br)? - OPCIONAL
                                                          # /cambio - FIXO
    def get_url_parametros(self):
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


if __name__ == '__main__':

    url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar" 
    extrator_url = ExtratorURL(url)
  
    valor_quantidade = extrator_url.get_valor_parametro('quantidade')
    valor_moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
    valor_moeda_destino = extrator_url.get_valor_parametro('moedaDestino')

    print(f'QUANTIDADE:     {valor_quantidade}')
    print(f'MOEDA ORIGEM:   {valor_moeda_origem}')
    print(f'MOEDA DESTINO:  {valor_moeda_destino}')