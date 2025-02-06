def iterativo(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def recursivo(numero):
    if numero == 0:
        return 1
    else:
        return numero * recursivo(numero - 1)

print(iterativo(5))
print(recursivo(5))