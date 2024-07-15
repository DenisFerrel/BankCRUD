from random import *

numeros_conta = []
            
while len(numeros_conta) != 5:
    numeros_conta.append(randrange(0,9))

for i in numeros_conta:
    print(i, end='')