meses = {'01': 31,'02' : 28, '03':31 , '04':30, '05':31, '06':30, '07':31, '08':31, '09':30, '10':31, '11':30, '12':31}
def dias_do_ano(data:str):
    dias=[]
    data.split('/')
    mes=data[3:5]
    dia=data[0:2]
    for i in range(1,int(mes)+1):
        if i<10:
            i='0'+str(i)
        else:
            i=str(i)
        dias.append(meses[i])
    dias=sum(dias)
    dias=dias-int(meses[mes])+int(dia)-1


    return dias


data='15/03/2019'
print(dias_do_ano(data))
