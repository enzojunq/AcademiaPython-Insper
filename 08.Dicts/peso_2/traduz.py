def traduz(palavras_eng,eng_2_port):
    portugues=[]
    for i in palavras_eng:
        for k,traducao in eng_2_port.items():
            if i==k:
                portugues.append(traducao)
    return portugues