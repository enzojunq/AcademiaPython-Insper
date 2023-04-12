while True:
    digite = input("Digite algo: ")
    if digite == 'bom dia':
        print("Bom dia")
    elif digite == 'oi':
        print('Olá!')
    elif digite == 'site':
        print("Acesse https://insper.edu.br")
    elif digite == 'blackboard':
        print("Lá temos materiais, notas e muito mais!")
    elif digite == 'tchau' or digite == 'encerrar':
        print("Até logo")
        break
    else:
        print('Não sei como te ajudar!')