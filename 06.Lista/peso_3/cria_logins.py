def login_disponivel(login,usuarios):
    if login not in usuarios:
        return login
    else:
        i=1
        while True:
            if login+f'{i}' not in usuarios:
                return login+f'{i}' 
            i+=1


lista=(['andre', 'fabio1'])
print(login_disponivel('fabio',['andre', 'fabio','fabio1']))