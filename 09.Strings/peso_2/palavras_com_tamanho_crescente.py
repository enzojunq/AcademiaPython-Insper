def palavras_com_tamanho_crescente(lista):
    for i in range(len(lista)-1):
        if len(lista[i+1])<=len(lista[i]):
            return False
    return True


lista = ['a', 'ab', 'abc', 'abcd']

print(palavras_com_tamanho_crescente(lista))