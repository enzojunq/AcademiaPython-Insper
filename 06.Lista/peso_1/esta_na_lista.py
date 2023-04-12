def esta_na_lista(pais,lista):
    for i in lista:
        if pais in i:
            return True
    return False
        
print(esta_na_lista('Brasil',['Brasil','Argentina','Chile','Uruguai']))