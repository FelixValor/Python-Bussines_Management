import Movimiento
class Cuenta:
    nCuenta=1
    
    def __init__(self,dni,nombre,saldo,listaMovimientos):
        self.nCuenta=Cuenta.nCuenta
        self.dni=dni
        self.nombre=nombre
        self.saldo=saldo
        self.listaMovimientos=listaMovimientos
        Cuenta.nCuenta +=1

    

    def imprimir_cuenta(self):
        mensaje=[]
        mensaje.append('Numero de cuenta: ',self.nCuenta)
        mensaje.append('DNI: ',self.dni)
        mensaje.append('Nombre: ',self.nombre)
        mensaje.append('Saldo: ',self.saldo)
        mensaje.append('---Lista de movimientos---')
        if len(self.listaMovimientos) >= 0:
            for m in self.listaMovimientos:
                mensaje.append("Fecha: ",m.fecha)
                mensaje.append("Cantidad: ",m.cantidad)
                if m.esIngreso==True:
                    mensaje.append("Tipo: Ingreso")
                else:
                    mensaje.append("Tipo: Retirada")
                mensaje.append("Concepto: ",m.concepto)
        else:
            mensaje.append("No existen movimientos en esta cuenta")
        return mensaje

    def hacer_movimiento(self,movimiento: Movimiento):
        self.listaMovimientos.append(movimiento)
        if movimiento.esIngreso:
            self.saldo=self.saldo+movimiento.cantidad
        else:
            self.saldo=self.saldo-movimiento.cantidad
        






