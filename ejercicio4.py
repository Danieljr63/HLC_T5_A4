def suma_digitos(numero):
    if numero == 0:
        return 0
    else:
        return numero % 10 + suma_digitos(numero // 10)

print(suma_digitos(1234))