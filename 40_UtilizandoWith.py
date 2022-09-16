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
    
    def __enter__(self):                               # COMANDOS MAGICOS __enter__() e __exit__()
        return self                                    # PERMITE A UTILIZACAO DO COMANDO with NO 
                                                       # ESCOPO DO MAIN AO INVES DO try, except, finally    
    def __exit__(self, type, valor, traceback):      
        print("fechando arquivo")


with LeitorDeArquivo("arquivo.txt") as leitor:       # COM objeto COMO alias
    leitor.ler_proxima_linha()                       # objeto.metodo()