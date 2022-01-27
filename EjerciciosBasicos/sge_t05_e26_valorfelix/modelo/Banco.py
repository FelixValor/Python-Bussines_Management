class Banco:
    def __init__(self,nombre,listaCuentas,saldoTotal):
        self.nombre=nombre
        self.listaCuentas=listaCuentas
        self.saldoTotal=saldoTotal
    
    def existe_cliente(self,dni):
        for cuenta in self.listaCuentas:
            if cuenta.dni == dni:
                return cuenta
            else:
                return None