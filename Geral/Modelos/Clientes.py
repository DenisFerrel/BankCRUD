from Contas import Conta
import mysql.connector


class Cliente():
    lista_de_clientes = []
    


# PROPRIEDADES DO CLIENTE:

    def __init__(self, nome, cpf, saldo_inicial=0):
        self._nome = nome
        self._cpf = cpf
        self._conta = Conta(saldo_inicial)
        self._ativo = False
        Cliente.lista_de_clientes.append(self)
        
        #CONEXÃO COM BANCO DE DADOS:

        conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Denis@@7982mysql',
        database='banco_denis'
    )

        cursor = conexao.cursor()

        # Obtendo o número da conta (supondo que você tenha um método para isso)
        numero_conta = self._conta._conta  # ou use um método apropriado se existir

        # CRUD da conta na database:
        comando = (
            f'INSERT INTO banco_contas (nome_cliente, cpf_cliente, numero_conta, saldo_conta, status_conta) '
            f'VALUES ("{self._nome}", "{self._cpf}", {numero_conta}, {0}, {int(self._ativo)})'
        )
        cursor.execute(comando)
        conexao.commit()  # Edita o BD

        # Fechar a conexão
        cursor.close()
        conexao.close()

    def __str__(self):
        return f'{self.nome} | {self.cpf} | {self.conta}' 

    @classmethod
    def listar_clientes(cls):
        if cls.lista_de_clientes:
            print("Lista de clientes:")
            for cliente in cls.lista_de_clientes:
                print(f"Nome: {cliente._nome}, CPF: {cliente._cpf}, Conta: {cliente._conta._conta}, Ativo: {cliente._ativo}")
        else:
            print("Nenhum cliente foi criado ainda.")


    @classmethod
    def criar_cliente(cls, nome, cpf, conta, ativo = False):
        nova_conta = Cliente(nome, cpf, conta)
        return nova_conta


    # Getter

    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    

    @property
    def conta(self):
        return self._conta   


    @property
    def ativo(self):
        return 'Conta Ativa' if self._ativo else 'Conta Inativa'
    



# INTERAÇÃO COM O CLIENTE:

    def ativar_cliente(self):
        self._ativo = not self._ativo
