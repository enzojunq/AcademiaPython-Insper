def capsLock(texto:str):
    texto_corrigido=''
    for letra in texto:
        if letra.upper()==letra:
            texto_corrigido+=letra.lower()
        else:
            texto_corrigido+=letra.upper()
    return texto_corrigido
