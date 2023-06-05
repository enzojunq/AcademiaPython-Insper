def quando_passa(programacao,programa):
    canais_c_programa={}
    for canais,horarios in programacao.items():
        for horario, programas in horarios.items():
                if programas == programa:
                    if horario not in canais_c_programa:
                        canais_c_programa[horario]=[canais]
                    else:
                        canais_c_programa[horario].append(canais)

    return canais_c_programa


programacao= {
    'Raposa TV': {
        '00h00': 'ModSim: Tudo é Possível',
        '01h00': 'Férias em Mathland',
        '07h00': 'Hora do Relaxamento',
        '15h00': 'Vale a Pena Rever a Matéria',
        '23h30': 'DesSoft: Hacking the Server'
    },
    'INN': {
        '08h00': 'Notícias do Campus',
        '10h00': 'Futuro: Intercâmbio',
        '12h00': 'Tele curso: Cálculo IV',
        '16h00': 'Os Mistérios de DesSoft',
        '20h00': 'Vale a Pena Rever a Matéria',
        '22h00': 'Culinária dos Salgados'
    },
    'Rede Insper TV': {
        '07h00': 'Hora do Relaxamento',
        '13h00': 'Campus em Foco',
        '16h00': 'Os Mistérios de DesSoft',
        '20h00': 'Hora do Relaxamento',
        '21h00': 'Futuro: Intercâmbio'
    }
}
programa = 'Hora do Relaxamento'

print(quando_passa(programacao,programa))