
class AdminMenu:

    def __init__(self,controller):
        self.controller=controller

    def printConsole(message):
        print(message)

    def showMenu():
        print("--------------------------OPCIONES-----------------------------")
        print("(1) Ver listado completo de socios.")
        print("(2) Insertar un nuevo socio")
        print("(3) Añadir a un socio su familia")
        print("(4) Ver listado completo de los próximos eventos")
        print("(5) Buscar eventos por fecha y mostrar toda su información")
        print("(6) Insertar un nuevo evento")
        print("(7) Ver el control de cuotas-socios por años")
        print("(8) Actualizar el control de cuotas-socio para el año en curso")
        print("(9) Realizar el pago de una cuota por DNI de socio")
        print("(0) Salir")
        print("---------------------------------------------------------------")
        return input()


    def askForNewPartner():
        print("Introduzca los datos necesarios para crear un nuevo socio:")
        print("Nombre completo: ")
        fullname=input()
        print("Direccion: ")
        address=input()
        print("Numero de telefono: ")
        phoneNumber=input()
        print("Correo electronico: ")
        email=input()
        print("DNI: ")
        dni=input()
        print("Contraseña: ")
        password=input()
        newPartner=[dni,password,None,None,fullname,address,phoneNumber,email]
        return newPartner

    def addToFamily():
        print("Introduzca el DNI del socio al que vamos a añadirle un familiar")
        dni=input()
        print("Introduzca el familiar a añadir")
        familyDNI=input()
        print("Introduzca el tipo de familiar")
        print("1. Hijo")
        print("2. Pareja")
        print("3. Padre")
        familytype=input()
        data=[dni,familyDNI,familytype]
        return data