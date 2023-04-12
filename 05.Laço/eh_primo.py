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
print(eh_primo(0))
