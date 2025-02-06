def recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * recursiva(base, exponente - 1)

print(recursiva(2, 3))