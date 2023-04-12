def login_disponivel(login,usuarios):
    if login not in usuarios:
        return login
    else:
        i=1
        while True:
            if login+f'{i}' not in usuarios:
                return login+f'{i}' 
            i+=1

login=input()
usuarios=[]
while login!='fim':
    usuario=login_disponivel(login,usuarios)
    usuarios.append(usuario)
    login=input()
    
for i in range(len(usuarios)):
    print(usuarios[i])