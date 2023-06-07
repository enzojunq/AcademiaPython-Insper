def conta_palavras2(frase):
    especiais = ['?','!','.',',']
    if len(frase)==0:
        return {}
    fraselow=frase.lower()
    contador={}
    for letra in fraselow:
        if letra in especiais:
            fraselow=fraselow.replace(letra,'')
    fraselow=fraselow.split(' ')
    for palavra in fraselow:
        contador.setdefault(palavra, 0)
        contador[palavra]+=1

    return contador


frase = "Qual caminho devo tomar? Eu não sei para onde ir! disse Alice. Se você não sabe onde quer ir, qualquer caminho serve. disse o Gato."
print(conta_palavras2(frase))
