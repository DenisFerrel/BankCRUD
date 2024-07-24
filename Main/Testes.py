from Modelos.Clientes import Cliente


cliente3 = Cliente.criar_conta('Ana', '1223.456', '771234-5')
cliente4 = Cliente.criar_conta('Julinho', '2345.543', '12345-6')
cliente3.ativar_conta()

Cliente.listar_clientes()