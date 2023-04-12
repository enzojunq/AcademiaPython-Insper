def maior_fator_primo(n): 
    fator = 2 # primeiro fator
    fatores=[]
    while n != 1:
        # conta a multiplicidade de fator em n
        mult = 0
        while n%fator == 0:
            n = n / fator
            mult = mult + 1

        # imprime a multiplicade do fator
        if mult != 0:
            # print("fator %d multiplicidade %d" %(fator, mult))
            fatores.append(fator)

        fator = fator + 1    
    return max(fatores)
print(maior_fator_primo(100))