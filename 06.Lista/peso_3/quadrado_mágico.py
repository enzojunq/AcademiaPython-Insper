
def quadrado_magico(quadrado):
    
    n=len(quadrado)

    soma_referencia=sum(quadrado[0])

    for i in range(n):
        if sum(quadrado[i]) != soma_referencia:
            return False
    
    for i in range(n):
        soma_coluna=0
        for j in range(n):
            soma_coluna+=quadrado[i][j]
        if soma_coluna!=soma_referencia:
            return False
    
    soma_diagonal=0
    for i in range(n):
        soma_diagonal+=quadrado[i][i]
    if soma_diagonal!=soma_referencia:
        return False
    
    soma_diagonal=0
    for i in range(n):
        soma_diagonal+=quadrado[i][n-1-i]
    if soma_diagonal!=soma_referencia:
        return False
    
    return True


    


    


    



quadrado = [ [6, 1, 8], [7, 5, 3], [2, 9, 4] ]
print(quadrado_magico(quadrado))