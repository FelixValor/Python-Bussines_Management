import imp
from src.util.Checker import Checker
import time
import os
import re

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

class AdminMenu:

    def __init__(self,controller):
        self.controller=controller

    def printConsole(message):
        print(message)

    
        

    def showMenu():
        valid=False
        
        print(bcolors.OKBLUE)
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
        print(bcolors.ENDC)
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


    def askForNewPartner(self):
        print(bcolors.OKBLUE+"Introduzca los datos necesarios para crear un nuevo socio:"+bcolors.ENDC)
        print(bcolors.OKCYAN+"Nombre completo: "+bcolors.ENDC)
        fullname=input()
        print(bcolors.OKCYAN+"Direccion: "+bcolors.ENDC)
        address=input()
        print(bcolors.OKCYAN+"Numero de telefono: "+bcolors.ENDC)
        phoneNumber=input()
        print(bcolors.OKCYAN+"Correo electronico: "+bcolors.ENDC)
        email=input()
        print(bcolors.OKCYAN+"DNI: "+bcolors.ENDC)
        dni=input()
        print(bcolors.OKCYAN+"Contraseña: "+bcolors.ENDC)
        password=input()
        newPartner=[dni,password,None,None,fullname,address,phoneNumber,email]
        self.pressAnyKeyToContinue()
        return newPartner

    def addToFamily():
        print(bcolors.OKBLUE+"Introduzca el DNI del socio al que vamos a añadirle un familiar"+bcolors.ENDC)
        dni=input()
        print(bcolors.OKCYAN+"Introduzca el familiar a añadir"+bcolors.ENDC)
        familyDNI=input()
        print(bcolors.OKCYAN+"Introduzca el tipo de familiar")
        print("1. Hijo")
        print("2. Pareja")
        print("3. Padre"+bcolors.ENDC)
        familytype=input()
        data=[dni,familyDNI,familytype]
        return data

    def addEvent():
        valid=False
        while(valid==False):
            print("Introduzca una fecha para el evento (dd/mm/yyyy):")
            eventDate = input()
            try:
                date1 = time.strptime(eventDate, '%d/%m/%Y')
                valid=True
            except ValueError:
                print(bcolors.FAIL+'¡Fecha no valida!'+bcolors.ENDC)
        #------------------------------------------#
        valid=False
        while(valid==False):
            print("Introduze la fecha maxima de inscripcion (dd/mm/yyyy):")
            maxDateInscription=input()
            try:
                date2 = time.strptime(maxDateInscription, '%d/%m/%Y')
                if(date1>date2):
                    valid=True
                else:
                    print(bcolors.FAIL+"La fecha maxima de inscripcion debe de ser menor a la del propio evento"+bcolors.ENDC)
            except ValueError:
                print(bcolors.FAIL+'¡Fecha no valida!'+bcolors.ENDC)
            
        print("Introduzca la ciudad en la que se organiza el evento:")
        city=input()
        print("Introduzca la provincia de ciudad indicada:")
        province=input()
        valid=False
        while(valid==False):
            print("Introduzca el DNI del socio que organiza el evento:")
            organizer=input()
            if(Checker.checkDNI(organizer)):
                if Checker.checkEventDay(eventDate,organizer)==False:
                    valid=True
                else:
                    print("Este organizador ya tiene a su cargo un evento")
                    
            else:
                print("Este dni no se corresponde a ningun socio")
            
        print("Introduce los kilometros que durara la ruta:")
        totalKM=input()
        print("Introduce el precio necesario para asistir al evento:")
        price=input()
        
        data=[eventDate,maxDateInscription,city,province,organizer,totalKM,price]
        return data