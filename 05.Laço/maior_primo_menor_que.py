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
def maior_primo_menor_que(num):
    if num < 2:
        return -1

    for i in range(num, 1, -1):
        if eh_primo(i):
            return i
print(maior_primo_menor_que(100))
