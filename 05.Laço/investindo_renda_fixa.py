def calcula_investimento(investimento_inicial,meses,ativo):
    if ativo == 'CDB':
        for i in range(1,meses+1):
            investimento_inicial = investimento_inicial * 1.013
            if i%6==0:
                investimento_inicial = investimento_inicial * 1.012
            
    elif ativo == 'LCI':
        for i in range(1,meses+1):
            investimento_inicial = investimento_inicial * 1.016
    elif ativo == 'LCA':
        for i in range(1,meses+1):
            investimento_inicial = investimento_inicial * 1.0145
            if i%4==0:
                investimento_inicial = investimento_inicial * 1.01
            
    return investimento_inicial
print(calcula_investimento(1000,10,'LCA'))
