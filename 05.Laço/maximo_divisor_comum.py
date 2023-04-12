def maximo_divisor_comum(a,b):
    if a == b:
        return a
    elif a > b:
        return maximo_divisor_comum(a-b,b)
    else:
        return maximo_divisor_comum(a,b-a)
print(maximo_divisor_comum(12,14))