def nome_usuario(email:str):
    pos=email.find('@')
    return email[:pos]