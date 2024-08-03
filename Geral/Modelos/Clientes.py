from Contas import Conta

class Cliente():
    lista_de_clientes = []

# PROPRIEDADES DO CLIENTE:

    def __init__(self, nome, cpf, saldo_inicial=0):
        self._nome = nome
        self._cpf = cpf
        self._conta = Conta(saldo_inicial)
        self._ativo = False
        Cliente.lista_de_clientes.append(self)

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

"""
cliente1 = Cliente('Livia', '37028525813', 1500)
cliente2 = Cliente('Denis', '41756168881', 2300)
cliente2.ativar_cliente()

Cliente.listar_clientes()
"""