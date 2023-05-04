def remove_vogais(texto):
    texto_corrigido=''
    for letra in texto:
        if letra.lower() in 'aeiou':
            texto_corrigido+=''
        else:
            texto_corrigido+=letra
    return texto_corrigido