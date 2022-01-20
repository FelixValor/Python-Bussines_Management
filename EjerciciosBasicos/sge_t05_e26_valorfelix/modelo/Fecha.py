from datetime import date


class Fecha:
    
    def __init__(self, dia=1,mes=1,annio=1900):
        self.dia=dia
        self.mes=mes
        self.annio=annio

    def fechaActual(self):
        self.dia=date.today().day
        self.mes=date.today().month
        self.annio=date.today().year
        print (self.dia)
        print (self.mes)
        print (self.annio)


f=Fecha()
f.fechaActual()