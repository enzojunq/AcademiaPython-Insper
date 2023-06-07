def perfis_profissionais(pessoas):
    trabalho = {}

    for pessoa, info in pessoas.items():
        ramo = info['ramo']
        salario = info['salário']
        anos = info['anos de serviço']
        email = info['e-mail']
        email = email.split('@')
        posicao = email[1].find('.')
        email = email[1][:posicao]

        if ramo not in trabalho:
            trabalho[ramo] = {'média salarial': [salario], 'tempo médio de serviço': [anos], 'servidores': [email]}
        else:
            trabalho[ramo]['média salarial'].append(salario)
            trabalho[ramo]['tempo médio de serviço'].append(anos)
            if email not in trabalho[ramo]['servidores']:
                trabalho[ramo]['servidores'].append(email)

    for ramo, info in trabalho.items():
        if len(info['média salarial']) >= 1:
            info['média salarial'] = int(sum(info['média salarial']) / len(info['média salarial']))
            info['tempo médio de serviço'] = (sum(info['tempo médio de serviço']) / len(info['tempo médio de serviço']))

    return trabalho


pessoas = {
    'Pedro Souza': {
        'ramo': 'secretariado',
        'salário': 2500,
        'anos de serviço': 3,
        'e-mail': 'pedro.paulo@hotmail.com'
    },
    'Marisa Monteiro': {
        'ramo': 'odontologia',
        'salário': 6000,
        'anos de serviço': 8,
        'e-mail': 'marisa_monteiro@gmail.com'
    },
    'Vitor Cerqueira': {
        'ramo': 'odontologia',
        'salário': 6000,
        'anos de serviço': 10,
        'e-mail': 'vitorcerqueira@gmail.com'
    },
    'Sandra Gomes': {
        'ramo': 'secretariado',
        'salário': 5000,
        'anos de serviço': 5,
        'e-mail': 'gomes-sandra@uol.com.br'
    },
    'Patrícia Ramos': {
        'ramo': 'vendas',
        'salário': 4000,
        'anos de serviço': 2,
        'e-mail': 'patricia-ramos-1990@yahoo.com.br'
    }
}

print(perfis_profissionais(pessoas))
