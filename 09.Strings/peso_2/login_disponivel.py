def login_disponivel(login,usuarios):
    if login not in usuarios:
        return login
    else:
        i=1
        while True:
            if login+f'{i}' not in usuarios:
                return login+f'{i}' 
            i+=1

nome='andre'
lista=(['andre','andre1', 'fabio'])

print(login_disponivel(nome,lista))