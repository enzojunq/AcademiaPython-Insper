def decodifica(sistema, palavra):
    palavra_deco=palavra
    for letra, letra_cod in sistema.items():
        if letra_cod in palavra_deco:
            palavra_deco=palavra_deco.replace(letra_cod,letra)
    return palavra_deco


sistema = {
    'a': 'z',
    'b': 'e',
    'z': '!',
    'e': '*',
}
palavra = 'eznznz'
print(decodifica(sistema, palavra))