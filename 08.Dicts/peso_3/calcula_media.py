def calcula_media(pessoas:dict,pais:str):
    media=[]
    for pessoa,dados in pessoas.items():
        if dados['nacionalidade']==pais:
            media.append(dados['idade'])
    valor_media=sum(media)/len(media)
    return valor_media
