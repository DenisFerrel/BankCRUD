


lista = []

a = 1
b = 2
c = 3

lista.append(a)
lista.append(b)
lista.append(c)

#print(lista)

def achar_numero(n):
    if n in lista:
        print('Achei o número')
    else:
        print('não achei o número')


achar_numero(4)