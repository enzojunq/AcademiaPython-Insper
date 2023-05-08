def anagrama(palavra1,palavra2):
    letras=[]
    if len(palavra1) != len(palavra2):
        return False
    for letra in palavra1:
        letras.append(letra)
    for letra in palavra2:
        if letra not in letras:
            return False
        else:
            letras.remove(letra)
    if len(letras) == 0:       
        return True
    else: 
        return False

palavra1='cacos'
palavra2='sacos'
print(anagrama(palavra1,palavra2))