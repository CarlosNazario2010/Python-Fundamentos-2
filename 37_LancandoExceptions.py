class OperacaoFinanceiraError(Exception):
    pass        
    

class  SaldoInsuficienteError(Exception):
  
    def __init__(self, message="", saldo=None, valor=None):
        self.saldo = saldo
        self.valor = valor
        msg = "Saldo insuficiente para efetuar uma transação \n"\
              f"Saldo atual: {self.saldo}. Valor a ser sacado: {self.valor}"
        self.msg  =  message or msg
        
        super(SaldoInsuficienteError, self).__init__ (self.msg)


class Cliente:
    
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:
    
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.__agencia =0
        self.__numero = 0
        self.saques_nao_permitidos = 0 
        self.transferencias_nao_permitidas = 0 
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30/ContaCorrente.total_contas_criadas


    @property
    def agencia(self):
        return self.__agencia

    def __set_agencia(self, value):
    
        if not isinstance(value, int):
            raise ValueError("O atributo agencia deve ser um inteiro", value)
        
        if value <= 0:
            raise ValueError("O atributo agencia deve ser maior que zero")            
        
        self.__agencia = value


    @property
    def numero(self):
        return self.__numero

    def __set_numero(self, value):
    
        if not isinstance(value, int):
            raise ValueError("O atributo número deve ser um inteiro")
    
        if value <= 0:
            raise ValueError("O atributo número  deve ser maior que zero")
    
        self.__numero = value


    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, value):
        
        if not isinstance(value, int):
            raise ValueError("O atributo saldo deve ser um inteiro")    
        
        self.__saldo = value


    def transferir(self, valor, favorecido):
    
        if valor < 0:
            raise ValueError("O valor a ser depositado não pode ser menor que zero")
    
        try:
            self.sacar(valor)
    
        except SaldoInsuficienteError as E:
            self.transferencias_nao_permitidas += 1
            E.args = ()
            raise OperacaoFinanceiraError("Operação não finalizada") from E
        
        favorecido.depositar(valor)


    def sacar(self, valor):
    
        if valor < 0:
            raise ValueError("O valor a ser sacado não pode ser menor que zero")
    
        if self.saldo < valor:
            self.saques_nao_permitidos+=1
            raise SaldoInsuficienteError("",saldo=self.saldo, valor=valor)
    
        self.saldo -= valor


    def depositar(self, valor):
        self.saldo += valor


if __name__ == '__main__':

    conta_corrente1 = ContaCorrente(None, 400, 1234567)
    conta_corrente2 = ContaCorrente(None, 401, 1234568)
    
    print('Conta Corrente 1 - saldo: ', conta_corrente1.saldo)
    print('Saque de 100 na Conta Corrente 1')
    conta_corrente1.sacar(100)
    print("Conta Corrente1 - saldo apos o saque: ",conta_corrente1.saldo)
    print()

    print('Conta Corrente 2 - saldo: ', conta_corrente2.saldo)
    print('Deposito de 100 na Conta Corrente 2')
    conta_corrente2.depositar(100)
    print("Conta Corrente2 - saldo apos o deposito: ",conta_corrente2 .saldo)
    print()

    print('Transferencia de 200 da Conta 2 para a Conta 1')
    conta_corrente2.transferir(200, conta_corrente1)
    print('Saldo da Conta 1 apos 200 de Transferencia: ', conta_corrente1.saldo)
    print('Saldo da Conta 2 apos 200 de Transferencia: ', conta_corrente2.saldo)