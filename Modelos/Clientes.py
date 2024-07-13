class Cliente():
    lista_de_clientes = []

    def __init__(self, nome, cpf, conta):
        self.nome = nome
        self.cpf = cpf
        self.conta = conta
        self._ativo = False
        Cliente.lista_de_clientes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.cpf} | {self.conta}' 

    @classmethod
    def listar_clientes(cls):
        for cliente in cls.lista_de_clientes:
            print(f'Nome: {cliente.nome} | CPF: {cliente.cpf} | Conta: {cliente.conta} | Status: {cliente.ativo}')

    # Getter
    @property
    def ativo(self):
        return 'Conta Ativa' if self._ativo else 'Conta Inativa'
    
    def ativar_conta(self):
        self._ativo = not self._ativo

cliente1 = Cliente('Denis', '123.456', '1234-5')
cliente1.ativar_conta()

Cliente.listar_clientes()
