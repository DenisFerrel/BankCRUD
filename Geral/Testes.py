import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'Modelos')))

from Modelos.Clientes import Cliente
from Modelos.Contas import Conta


cliente4 = Cliente('Marcos', '123456789')
cliente5 = Cliente('Breno', '987654321')
cliente6 = Cliente('Sandro', '123789456')

cliente4.ativar_cliente()
cliente6.ativar_cliente()


# Cliente.listar_clientes()





# TO DOs:

"""

1) Criar clientes novos: OK

2) Criar uma conta e acoplá-la ao Cliente novo: OK

3) Criar um arquivo SQL que armazene as contas criadas e gerencie seu cadastro e
saldo:

    - Criar a conexão e salvar no DB: ok
    - Criar método que verifica se existe um cliente cadastrado já e nega novo
      cadastro: ok
    - Criar método que ve se o número da conta já existe e cria outro: ok
    - Criar método que atualiza o status da conta no próprio DB:
    - Criar métodos que atualizam saldos e interações no próprio DB:

4) Criar um arquivo individual para cada cliente com histórico de saques/depósitos
e que cuspa o saldo ao final de todas essas operações:

5) Criar um layout HTML com CRUD para criação de clientes e movimentações bancárias











"""