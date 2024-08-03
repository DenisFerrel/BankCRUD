from Modelos.Clientes import Cliente
from Modelos.Contas import Conta

"""
cliente3 = Cliente.criar_cliente('Claudia', '1223.456', '771234-5')
cliente4 = Cliente.criar_cliente('Marcelo', '2345.543', '12345-6')

cliente3.ativar_cliente()

Cliente.listar_clientes()
"""

conta1 = Conta(1000)
conta2 = Conta(500)

conta1.deposito_conta(1500)
conta1.saque_conta(500)

conta1.ver_saldo()
conta2.ver_saldo()

Conta.listar_contas()