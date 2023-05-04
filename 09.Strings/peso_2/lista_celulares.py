def lista_celulares(celulares):
    lista=[]
    for celular in celulares:
        pais=celular.replace('+55','')
        if pais[2]=='9' and len(pais)==11:
            lista.append(pais[2:])
        elif pais[0]=='9' and len(pais)==9:
            lista.append(pais)



    return lista


celulares = (['+5511912345678','+5511912345678', '1155556666', '77778888', '+551133334444', '918273645', '11987654321']) 
#deve retornar a lista ['912345678', '918273645', '987654321']
print(lista_celulares(celulares))