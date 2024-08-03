import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'Modelos')))

from Modelos.Clientes import Cliente


cliente1 = Cliente('Livia', '37028525813', 1500)
cliente2 = Cliente('Denis', '41756168881', 2300)

Cliente.listar_clientes()

