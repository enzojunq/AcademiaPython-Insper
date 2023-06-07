import math
def quanto_tempo(tempos):
    hours = 0
    minutes = 0
    seconds = 0

    hms=['h','m','s']

    for tempo in tempos:
        if tempo == '':
            continue
        if 's' in tempo and 'm' in tempo and 'h' in tempo:
            posicao_s=tempo.find('s')
            posicao_m=tempo.find('m')
            posicao_h=tempo.find('h')
            segundos = tempo[posicao_m+1:posicao_s]
            minutos = tempo[posicao_h+1:posicao_m]
            horas = tempo[:posicao_h]
            seconds+=int(segundos)
            minutes+=int(minutos)
            hours+=int(horas)
        
        elif 's' in tempo and 'm' in tempo:
            posicao_s=tempo.find('s')
            posicao_m=tempo.find('m')
            segundos = tempo[posicao_m+1:posicao_s]
            minutos = tempo[:posicao_m]
            seconds+=int(segundos)
            minutes+=int(minutos)

        elif 'h' in tempo and 'm' in tempo:
            posicao_m=tempo.find('m')
            posicao_h=tempo.find('h')
            minutos = tempo[posicao_h+1:posicao_m]
            horas = tempo[:posicao_h]
            minutes+=int(minutos)
            hours+=int(horas)
        
        elif 'h' in tempo and 's' in tempo:
            posicao_s=tempo.find('s')
            posicao_h=tempo.find('h')
            segundos = tempo[posicao_h+1:posicao_s]
            horas = tempo[:posicao_h]
            seconds+=int(segundos)
            hours+=int(horas)

        elif 's' in tempo:
            posicao_s=tempo.find('s')
            segundos = tempo[:posicao_s]
            seconds+=int(segundos)

        elif 'm' in tempo:
            posicao_m=tempo.find('m')
            minutos = tempo[:posicao_m]
            minutes+=int(minutos)

        elif 'h' in tempo:
            posicao_h=tempo.find('h')
            horas = tempo[:posicao_h]
            hours+=int(horas)

    if seconds > 59:
        minutes+=math.floor(seconds/60)
        segundos_restantes =  seconds%60
        seconds = segundos_restantes
    
    if minutes > 59:
        hours+=math.floor(minutes/60)
        minutos_restantes =  minutes%60
        minutes = minutos_restantes

    if seconds ==0 and minutes ==0:
        return str(hours)+'h'
    elif seconds ==0 and hours ==0:
        return str(minutes)+'m'
    elif minutes ==0 and hours ==0:
        return str(seconds)+'s'
    elif seconds ==0:
        return str(hours)+'h'+str(minutes)+'m'
    elif minutes ==0:
        return str(hours)+'h'+str(seconds)+'s'
    elif hours ==0:
        return str(minutes)+'m'+str(seconds)+'s'
    else:
        return str(hours)+'h'+str(minutes)+'m'+str(seconds)+'s'
    



tempos = ['1h30s', '2h15s', '180m']
print(quanto_tempo(tempos))

# '1h2m20s'