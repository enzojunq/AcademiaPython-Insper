def apaga_repetidos(frase:str):
    used=''
    nova_frase=''
    for letra in frase:
        if letra not in used:
            used+=letra
            nova_frase+=letra
        else:
            nova_frase+='*'
    return nova_frase

teste='Um mago nunca se atrasa, nem se adianta, ele chega exatamente quando pretende chegar'


print(apaga_repetidos(teste))
