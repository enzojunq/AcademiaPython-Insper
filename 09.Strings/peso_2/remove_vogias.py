vogais = 'aeiou'
def remove_vogais(palavra):
    nova_palavra=''
    for letra in palavra:
        if letra not in vogais:
            nova_palavra+=letra
    return nova_palavra

palavra='enzo'
print(remove_vogais(palavra))

