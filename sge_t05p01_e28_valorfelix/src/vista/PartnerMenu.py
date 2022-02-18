
from multiprocessing.connection import answer_challenge


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class PartnerMenu:
    
    def __init__(self,controller):
        self.controller=controller

    def printConsole(message):
        print(bcolors.HEADER,end ="")
        print(message)
        print(bcolors.ENDC,end ="")

    def printErrorConsole(message):
        print(bcolors.FAIL,end ="")
        print(message)
        print(bcolors.ENDC,end ="")

    def showMenu():
        print(bcolors.OKBLUE+"--------------------------OPCIONES-----------------------------")
        print("(1) Ver mis próximos eventos y la lista de inscritos.")
        print("(2) Ver y apuntarme a eventos abiertos.")
        print("(3) Ver mis bicicletas.")
        print("(4) Ver mis reparaciones/mantenimientos.")
        print("(5) Añadir nueva bicicleta.")
        print("(6) Añadir reparación/mantenimiento a una de mis bicicletas.")
        print("(7) Ver mi familia.")
        print("(8) Ver mi histórico y estado de cuotas con toda su información.")
        print("(0) Salir")
        print("---------------------------------------------------------------"+bcolors.ENDC)
        order=input()
        try:
            if int(order) >= 0 and int(order) <= 9:
                pass
            else:
                print(bcolors.FAIL+"Debe de introducir numeros del 0 al 9"+bcolors.ENDC)
                input("Pulse intro para continuar...")
        except ValueError:
            print(bcolors.FAIL+"Introduzca solamente numeros"+bcolors.ENDC)
            input("Pulse intro para continuar...")
        return order
    
    def askIfJoin(amountEvents):
        print(bcolors.OKGREEN+"Deseas unirte a algun evento(SI/NO)"+bcolors.ENDC)
        answer=input()
        correct=False
        idEvent=-1
        while(correct==False):
            if(answer.upper()=="SI" or answer.upper()=="NO"):
                correct=True
                if(answer.upper()=="SI"):
                    print(bcolors.OKGREEN+"Introduzca el identificador del evento al que desea unirse:"+bcolors.ENDC)
                    idEvent=input()
                    try:
                        if int(idEvent) < 1 or int(idEvent) > amountEvents:
                            correct=False
                            print(bcolors.FAIL+"Introduzca un identificador valido"+bcolors.ENDC)
                        else:
                            print("funciona")
                    except ValueError:
                        correct=False
                        print(bcolors.FAIL+"Introduzca unicamente numeros"+bcolors.ENDC)
            else:
                print(bcolors.FAIL+"Responda solo SI o NO"+bcolors.ENDC)
                print(bcolors.OKGREEN+"Deseas unirte a algun evento(SI/NO)"+bcolors.ENDC)
                answer=input()
        return idEvent
