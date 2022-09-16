class LeitorDeArquivo:
  
    def __init__(self, arquivo):
        self.arquivo = arquivo
        print(f'Abrindo arquivo: {self.arquivo}')
    
    def ler_proxima_linha(self):
        print('Lendo linha ...')
        raise IOError()
        return 'Linha de arquivo'

    def fechar(self):
        print('Fechando arquivo.')
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, valor, traceback):
        print("fechando arquivo")


try:
    leitor = LeitorDeArquivo("arquivo.txt")       # try - TENTA EXECUTAR A ACAO
    leitor.ler_proxima_linha()

except IOError as err:                          # except - LANCA A EXCESSAO -
      raise err                                     # IOError - ERRO DE INPUT OU OUTPUT NO CASO 

finally:
      leitor.fechar()                               # O COMANDO finally OCORRERA INDEPENDENTEMENTE
                                                # SE LANCADA OU NAO A EXCESSAO 