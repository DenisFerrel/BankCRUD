from Contas import Conta
from Contas import Conexao_DB


class Cliente():

# PROPRIEDADES DO CLIENTE:

    def __init__(self, nome, cpf, saldo_inicial=0):
        self._nome = nome
        self._cpf = cpf
        self._conta = Conta(saldo_inicial)
        self._ativo = False
        
        #Faz a conexão
        conexao = Conexao_DB()
        cursor = conexao.cursor()
        
        # Obtendo o número da conta
        numero_conta = self._conta._conta  

        # CRUD da conta na database:
        
        comando_verificacao = (
            f'SELECT COUNT(*) FROM banco_contas WHERE nome_cliente = "{self._nome}" '
            f'AND cpf_cliente = "{self._cpf}"'
        )
        cursor.execute(comando_verificacao)
        resultado = cursor.fetchone()

        # Se não houver um registro correspondente, insira os novos dados
        if resultado[0] == 0:
            comando = (
                f'INSERT INTO banco_contas (nome_cliente, cpf_cliente, numero_conta, saldo_conta, status_conta) '
                f'VALUES ("{self._nome}", "{self._cpf}", {numero_conta}, {0}, {int(self._ativo)})'
                )
            cursor.execute(comando)
            conexao.commit()  # Edita o BD
            print("Conta criada com sucesso!")
        else:
            print("Erro: Já existe uma conta com este nome e CPF.")

        # Fechar a conexão
        cursor.close()
        conexao.close()

    def __str__(self):
        return f'{self.nome} | {self.cpf} | {self.conta}' 

    @classmethod
    def listar_clientes(cls):
        
        conexao = Conexao_DB()
        cursor = conexao.cursor()
        
        comando_listar= (f'SELECT * FROM banco_contas')
        cursor.execute(comando_listar)
        resultado = cursor.fetchall() #Le o banco de dados
        print(resultado)

        # Fechar a conexão
        cursor.close()
        conexao.close()
        
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

        #Faz a conexão
        conexao = Conexao_DB()
        cursor = conexao.cursor()
        
        ativar_cliente= f'UPDATE banco_contas SET status_conta = 1 WHERE nome_cliente = "{self._nome}"'
        cursor.execute(ativar_cliente)
        conexao.commit() #Edita banco de dados

        # Fechar a conexão
        cursor.close()
        conexao.close()
