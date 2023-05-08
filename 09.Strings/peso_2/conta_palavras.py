pontuacoes=['!','?','.',',']
def conta_palavras(frase:str):
    contagem={}
    nova_frase=frase
    for pontuacao in pontuacoes:
        nova_frase=nova_frase.replace(pontuacao,'')
    nova_frase=nova_frase.split(' ')
    for palavra in nova_frase:
        palavra=palavra.lower()
        if palavra not in contagem:
            contagem[palavra]=1
        else:
            contagem[palavra]+=1
        ### SORTED DE DICT ###
    contagem = dict(sorted(contagem.items(), key=lambda item: (item[1],item[0]), reverse=True))
    
    # pais_campeao= sorted (ouro.items(),key=lambda x: (x[1], prata[x[0]], bronze[x[0]]), reverse=True)
    return contagem

string = "Qual caminho devo tomar? Eu não sei para onde ir! Disse Alice. Se você não sabe onde quer ir, qualquer caminho serve. Disse o Gato."
print(conta_palavras(string))