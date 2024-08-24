
from random import randrange
import mysql.connector
from mysql.connector import Error

def Conexao_DB():
    #CONEXÃO COM BANCO DE DADOS:
    try:
            conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Denis@@7982mysql',
                database='banco_denis'
            )
            if conexao.is_connected():
                return conexao
    except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

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
    
    # Cria um numero de conta aleatório para um novo cliente
    @staticmethod
    def criar_conta():
        while True:
            # Geração de um número de conta aleatório
            numeros_conta = [str(randrange(0, 10)) for _ in range(5)]
            numero_conta = int(''.join(numeros_conta))
            
            
            #Faz a conexão
            conexao = Conexao_DB()
            cursor = conexao.cursor()
            
            # Verificar se o número da conta já existe no banco de dados
            comando = f"SELECT COUNT(*) FROM banco_contas WHERE numero_conta = {numero_conta}"
            cursor.execute(comando)
            resultado = cursor.fetchone()

            # Se o número da conta não existir, sair do loop e retornar o número
            if resultado[0] == 0:
                cursor.close()
                conexao.close()
                return numero_conta

            # Fecha a conexão antes de tentar novamente
            cursor.close()
            conexao.close()

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


    
"""
conta1 = Conta(1000)
conta2 = Conta(500)

conta1.deposito_conta(1500)
conta1.saque_conta(500)

conta1.ver_saldo()
conta2.ver_saldo()

Conta.listar_contas()
"""
