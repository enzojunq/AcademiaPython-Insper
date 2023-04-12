def eh_primo(x):
    cont=2
    if(x<=1):
        return False   
    else:
        while (cont<x):
            if x%cont==0:
                return False
            cont+=1
        else:
            return True
def proximo_primo(n):
    while True:
        n += 1
        if eh_primo(n):
            return n
print(proximo_primo(3))