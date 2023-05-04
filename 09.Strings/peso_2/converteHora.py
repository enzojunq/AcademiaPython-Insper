def converteHora(hora):
    horas = hora.split(":")
    if int(horas[0])>12:
        return '0'+ str(int(horas[0])-12) + ":" + horas[1] + " PM"
    elif horas[0] == '12':
        return str(hora) + " PM"
    else:
        return str(hora) + " AM"
    

hora = '15:30'
print(converteHora(hora))