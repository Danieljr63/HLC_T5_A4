def contar(numero):
    if numero < 10:
        return 1
    return 1 + contar(numero / 10)

print(contar(1234))