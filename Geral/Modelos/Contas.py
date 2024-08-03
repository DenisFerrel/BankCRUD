
from random import randrange

class Conta():
    numeros_conta = []

# PROPRIEDADES DA CONTA:

    def __init__(self, saldo = 0):
        self._conta = self.criar_conta()
        Conta.numeros_conta.append(self)
        self._saldo = saldo

    def __str__(self):
        return self._conta
    

    @property
    def conta(self):
        return self._conta
    
    @property
    def saldo(self):
        return self._saldo
    
    #Lista as contas existentes:
    @classmethod
    def listar_contas(cls):
        if cls.numeros_conta:
            for conta in cls.numeros_conta:
                print(f'Conta {conta._conta}, Saldo: {conta._saldo}')
        else:
            print('Nenhuma conta criada ainda.')


    # Cria um numero de conta aleatório para um novo cliente
    @staticmethod
    def criar_conta():
        numeros_conta = []
        while len(numeros_conta) != 5:
            numeros_conta.append(randrange(0,9))
        return int(''.join(map(str, numeros_conta)))
            
          

# INTERAÇÃO COM A CONTA:


    #Faz transferência entre 2 contas.    
    def transferir(self, valor, conta_destino):
        if conta_destino in Conta.numeros_conta:
            if 0 < valor <= self._saldo:
                self.saque_conta(valor)
                conta_destino.deposito_conta(valor)
                print(f"Transferência de {valor} para a conta {conta_destino._conta} realizada com sucesso.")
            else:
                print("Valor de transferência inválido. Verifique seu saldo ou o valor informado.")
        else:
            print("Conta de destino não encontrada.")


    #Saca da conta
    def saque_conta(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f'Valor de R$ {valor} sacado com sucesso')
        else:
            print('saldo insuficiente.')

    #Deposita na conta
    def deposito_conta(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'Depósito de R$ {valor} realizado com sucesso.')
        else:
            print('Depósito inválido. Favor tentar novamente')

    #Vê o saldo da conta
    def ver_saldo(self):
        return print(f'Saldo na conta {self._conta} de R$ {self._saldo}')


    



