def detectar_acao(users: dict, stop_words: list) -> dict:
    # Cria uma lista com os nomes dos usuários
    actions = {x: [] for x in users}
    pattern = ['ar', 'er', 'ir', 'or']

    for name, des in users.items():
        for feedback in des.values():
            # Separa as palavras das frases em uma lista
            feedback = feedback.split(' ')

            # Remove as stop_words das frases
            feedback = [x for x in feedback if x not in stop_words]

            for i, value in enumerate(feedback):
                # Verifica se a palavra é a ultima da string e se é um verbo e adiciona no dicionario
                if i == len(feedback) - 1 and value[-2:] in pattern:
                        actions[name].append(value)
                # Verifica se é um verbo e adiciona no dicionário de ações com a próxima palavra
                elif value[-2:] in pattern:
                    actions[name].append(value + ' ' + feedback[i+1])

    return actions

dicio = {
    'zezin1': {
        '2020-11-05 08:15:30': 'produto ruim vou processar já vocês',
        '2020-11-05 08:16:01': 'é um absurdo',
        '2020-11-05 08:18:09': 'pode enviar no meu email por favor?',
    },
    'mariarita': {
        '2020-10-01 05:05:00': 'gostaria de comprar um sofá',
        '2020-10-01 05:05:09': 'quais formas de pagamento aceitam?',
        '2020-10-01 05:08:39': 'conseguem entregar na minha moradia',
        '2020-10-01 06:01:03': 'mesmo que seja em uma chácara?',
    },
    'juca123': {
        '2021-02-09 05:05:00': 'perdi o boleto de pagamento',
        '2021-02-09 05:05:09': 'e ainda nao sei usar pix',
        '2021-02-09 05:08:39': 'poderiam emitir o boleto novamente',
        '2020-02-09 06:01:03': 'e mandar pro meu email',
    }
}

stopw = [
    'vou', 'meu', 'minha', 'o', 'pro',
    'para', 'já', 'é', 'no', 'na',
    'uma', 'por', 'um', 'e', 'em'
]

print(detectar_acao(dicio, stopw))
