'''
Created on Jan 23, 2017
@author: Arnaldo Quintero 13-11150
         Rafael Blanco 13-10156
'''

import datetime,math

class Tarifa:
    def __init__(self,semana,finSemana):
        self.tarifaSemana = semana
        self.tarifaFinSemana = finSemana

def calcularMonto(hora,tarifa,day):
    if (day<5):
        return hora*tarifa.tarifaSemana
    else:
        return hora*tarifa.tarifaFinSemana

def calcularPrecio(tarifa: Tarifa, tiempoServicio: [datetime.datetime]) -> float:
    inicio = tiempoServicio[0]
    fin = tiempoServicio[1]

    serv = math.ceil((fin - inicio).days*24*60 + (fin-inicio).seconds/60)
    cobro = 0
    if (serv<15):
        return 0
    elif (serv > 7*24*60):
        return -1
    else:

        day = inicio.weekday()

        while (serv>=24*60):
            cobro += calcularMonto(24,tarifa,day)
            serv -= 24*60
            day = (day+1)%7

        if (fin.minute > inicio.minute):
            cobro += (math.ceil(calcularMonto((serv/60),tarifa,day)))

        else:
            cobro += (math.floor(calcularMonto((serv/60),tarifa,day)))

        return cobro

i = datetime.datetime(2017,1,22,23,50)
j = datetime.datetime(2017,1,23,00,5)
tarifa = Tarifa(1,10)
print (calcularPrecio(tarifa,[i,j]))
