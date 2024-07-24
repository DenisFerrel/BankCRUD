
class Cliente():
    lista_de_clientes = []

# PROPRIEDADES DO CLIENTE:

    def __init__(self, nome, cpf, conta):
        self._nome = nome
        self._cpf = cpf
        self._conta = conta
        self._ativo = False
        Cliente.lista_de_clientes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.cpf} | {self.conta}' 

    
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

    @classmethod
    def listar_clientes(cls):
        for cliente in cls.lista_de_clientes:
            print(f'Nome: {cliente.nome} | CPF: {cliente.cpf} | Conta: {cliente.conta} | Status: {cliente.ativo}')


    def ativar_conta(self):
        self._ativo = not self._ativo

    @classmethod
    def criar_cliente(cls, nome, cpf, conta, ativo = False):
        nova_conta = Cliente(nome, cpf, conta)
        return nova_conta



