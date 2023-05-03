def palavras_sao_iguais(palavra:str):
    pos=palavra.find('-')
    parte_1=palavra[:pos]
    parte_2=palavra[pos+1:]
    if parte_1==parte_2:
        return True
    else:
        return False
    
print(palavras_sao_iguais('reco-reco'))