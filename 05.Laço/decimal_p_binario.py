def decimal_para_binario(n):
    decimal=[]
    if n <0:
        return 'Negativo'
    else:
        while n>0:
            if n%2==0:
                decimal.append('0')
            else:
                decimal.append('1')
            n=n//2
        decimal.reverse()
        return ''.join(decimal)
print(decimal_para_binario(10))