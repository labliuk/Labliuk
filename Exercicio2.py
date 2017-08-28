lista = []

for i in range(0,20):
        a = int(input("Digite um numero: "))
        lista.append(a)

def troca(lista):
    c = 0
    for i in lista:
        if i < 0:
            lista[c] = 0
        elif i > 0 and i < 10:
            lista[c] = 1
        else:
            lista[c] = 2
        c = c+1
    return lista

lista = troca(lista)

print (lista)
