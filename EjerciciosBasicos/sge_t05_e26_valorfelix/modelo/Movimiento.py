#from Sge_env_EjerciciosPython.EjerciciosBasicos.sge_t05_e26_valorfelix.modelo.modelo_fecha import Fecha
import Fecha

class Movimiento:
    def __init__(self,cantidad,esIngreso,concepto):
        self.fecha=Fecha.fechaActual()
        self.cantidad=cantidad
        self.esIngreso=esIngreso
        self.concepto=concepto
