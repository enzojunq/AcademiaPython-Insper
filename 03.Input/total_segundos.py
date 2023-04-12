dias=int(input())
horas=int(input())
minutos=int(input())
segundos=int(input())

dias=dias*86400
horas=horas*3600
minutos=minutos*60
total=dias+horas+minutos+segundos

print(total)