import datetime,math

class Tarifa:
    def __init__(self,semana,finSemana):
        self.tarifaSemana = semana
        self.tarifaFinSemana = finSemana

class Servicio:

    def calcularMonto(horas: int, cobro: float)->int:
        #print ("Monto a Pagar: " + horas*cobro)
        return horas*cobro

    def calcularPrecio(tarifa: Tarifa, tiempoServicio: [datetime.datetime]) -> float:
        horaF = datetime.time(23,59,59,999)
        inicio = tiempoServicio[0]
        fin = tiempoServicio[1]

        if (inicio.month != fin.month):

            #para el mes del inicio
            horasi = 24 - inicio.hour
            sumai=0
            temp = inicio.weekday()

            if (inicio.month in (1,3,5,7,8,10,12)):
                i= 31 - inicio.day

            elif (inicio.month==2):
                if (inicio.year%4 == 0):
                    i = 29 - inicio.day
                else:
                    i = 28 - inicio.day
            else:
                i = 30 - inicio.day

            while i-1 > 0 and i<=7:
                temp+=1
                if (temp<5):
                    cobrot = tarifa.tarifaSemana
                else:
                    cobrot = tarifa.tarifaFinSemana
                sumai += Servicio.calcularMonto(24,cobrot)
                i-=1

            if (i>7):
                return "ERROR"


            #para el mes de fin
            if ((fin.minute - inicio.minute)>0):
                horasf = fin.hour
            else:
                horasf = fin.hour - 1

            j = fin.day
            sumaf = 0
            temp = fin.weekday()
            while j-1 > 0 and i<=7:
                temp-=1
                if (temp<5):
                    cobrot = tarifa.tarifaSemana
                else:
                    cobrot = tarifa.tarifaFinSemana
                sumaf += Servicio.calcularMonto(24,cobrot)
                i-=1

            if (i>7):
                return "ERROR"

            return horasf+horasi+sumai+sumaf


        else:
            if (fin.day == inicio.day):

                if (fin.hour != inicio.hour):

                    horas  = fin.hour - inicio.hour - 1

                    if ((fin.minute - inicio.minute)>=0):
                        minutos = fin.minute - inicio.minute
                    else:
                        minutos = 60 - abs(fin.minute - inicio.minute)

                    tiempo = horas + math.ceil(minutos/60)

                else:

                    minutos = fin.minute - inicio.minute
                    if (minutos>=15):
                        tiempo = 1
                    else:
                        tiempo = 0

                if (fin.weekday()<5):
                    cobro = tarifa.tarifaSemana
                else:
                    cobro = tarifa.tarifaFinSemana

                return Servicio.calcularMonto(tiempo,cobro)

            else:

                if(fin.day - inicio.day == 1):

                    horasi = 24 - inicio.hour
                    if ((fin.minute - inicio.minute)>0):
                        horasf = fin.hour
                    else:
                        horasf = fin.hour - 1

                    if (fin.weekday()<5):
                        cobrof = tarifa.tarifaSemana
                    else:
                        cobrof = tarifa.tarifaFinSemana

                    if (inicio.weekday()<5):
                        cobroi = tarifa.tarifaSemana
                    else:
                        cobroi = tarifa.tarifaFinSemana

                    return Servicio.calcularMonto(horasf,cobrof)+Servicio.calcularMonto(horasi,cobroi)

                else:

                    horasi = 24 - inicio.hour
                    if ((fin.minute - inicio.minute)>0):
                        horasf = fin.hour
                    else:
                        horasf = fin.hour - 1

                    if (fin.weekday()<5):
                        cobrof = tarifa.tarifaSemana
                    else:
                        cobrof = tarifa.tarifaFinSemana

                    if (inicio.weekday()<5):
                        cobroi = tarifa.tarifaSemana
                    else:
                        cobroi = tarifa.tarifaFinSemana

                    i = fin.day - inicio.day
                    suma=0
                    temp = inicio.weekday()
                    while i-1 > 0 and i<=7:
                        temp += 1
                        if (temp<5):
                            cobrot = tarifa.tarifaSemana
                        else:
                            cobrot = tarifa.tarifaFinSemana
                        suma += Servicio.calcularMonto(24,cobrot)
                        i-=1

                    if (i>7):
                        return "ERROR"

                    return suma+Servicio.calcularMonto(horasf,cobrof)+Servicio.calcularMonto(horasi,cobroi)


#i = datetime.datetime(2017,1,22,10,45)
#j = datetime.datetime(2017,1,23,12,40)
#tarifa = Tarifa(10,100)
#print (Servicio.calcularPrecio(tarifa,[i,j]))
