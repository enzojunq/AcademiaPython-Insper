def conserta_teclado(palavra_corrompida):
    palavra_certa=''
    for i in range(len(palavra_corrompida)):
        if palavra_corrompida[i].lower() != palavra_corrompida[i-1].lower():
            palavra_certa+=palavra_corrompida[i].lower()
    return palavra_certa

palavra='pppaaalllaavvrraa'
print(conserta_teclado(palavra))