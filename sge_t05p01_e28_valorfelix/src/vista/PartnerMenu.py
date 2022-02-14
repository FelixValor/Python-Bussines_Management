class PartnerMenu:
    
    def __init__(self,controller):
        self.controller=controller

    def printConsole(message):
        print(message)

    def showMenu():
        print("--------------------------OPCIONES-----------------------------")
        print("(1) Ver mis próximos eventos y la lista de inscritos.")
        print("(2) Ver y apuntarme a eventos abiertos.")
        print("(3) Ver mis bicicletas.")
        print("(4) Ver mis reparaciones/mantenimientos.")
        print("(5) Añadir nueva bicicleta.")
        print("(6) Añadir reparación/mantenimiento a una de mis bicicletas.")
        print("(7) Ver mi familia.")
        print("(8) Ver mi histórico y estado de cuotas con toda su información.")
        print("(0) Salir")
        print("---------------------------------------------------------------")
        return input()