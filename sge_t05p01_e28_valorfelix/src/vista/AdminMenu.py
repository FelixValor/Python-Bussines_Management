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
        print(bcolors.HEADER,end ="")
        print(message)
        print(bcolors.ENDC,end ="")

    def printErrorConsole(message):
        print(bcolors.FAIL,end ="")
        print(message)
        print(bcolors.ENDC,end ="")
            

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

    def askForDNIToPay():
        b=True
        while(b):
            print(bcolors.OKBLUE+"Introduce el DNI del socio que va a pagar su cuota: "+bcolors.ENDC)
            dni=input()
            if(Checker.checkDNI(dni) and dni!="11111111K"):
                b=False
            elif dni=="11111111K":
                print(bcolors.FAIL+"El administrador no tiene que pagar cuotas"+bcolors.ENDC)
            else:
                print(bcolors.FAIL+"Introduzca un DNI existente"+bcolors.ENDC)
        return dni
            

    def askForNewPartner():
        
        print(bcolors.OKBLUE+"Introduzca los datos necesarios para crear un nuevo socio:"+bcolors.ENDC)
        print(bcolors.OKCYAN+"Nombre completo: "+bcolors.ENDC)
        fullname=input()
        
        print(bcolors.OKCYAN+"Direccion: "+bcolors.ENDC)
        address=input()
        valid=False
        while(valid==False):
            print(bcolors.OKCYAN+"Numero de telefono: "+bcolors.ENDC)
            phoneNumber=input()
            if Checker.verifyPhone(phoneNumber):
                valid=True
            else:
                print(bcolors.FAIL+"Introduzca un numero de telefono valido"+bcolors.ENDC)
        
        valid=False
        while(valid==False):
            print(bcolors.OKCYAN+"Correo electronico: "+bcolors.ENDC)
            email=input()
            if Checker.isValidEmail(email):
                valid=True
            else:
                print(bcolors.FAIL+"Introduzca un email valido"+bcolors.ENDC)

        valid=False
        while(valid==False):
            print(bcolors.OKCYAN+"DNI: "+bcolors.ENDC)
            dni=input()
            
            if Checker.checkDNI(dni):
                print(bcolors.FAIL+"Introduzca un DNI que no exista previamente en el sistema"+bcolors.ENDC)
            else:
                if Checker.verifyDNI(dni):
                    valid=True
                else:
                    print(bcolors.FAIL+"Introduzca un DNI valido"+bcolors.ENDC)
                
        
        print(bcolors.OKCYAN+"Contraseña: "+bcolors.ENDC)
        password=input()
        
        valid=False
        isAdmin=False
        while(valid==False):
            print(bcolors.OKCYAN+"¿Es administrador?(S/N) "+bcolors.ENDC)
            answer=input()
            if answer.lower()=="s" or answer.lower()=="n":
                if answer.lower()=="s":
                    isAdmin=True
                valid=True
            else:
                print(bcolors.FAIL+"Introduzca una respuesta valida (S/)"+bcolors.ENDC)

        newPartner=[dni,password,None,isAdmin,fullname,address,phoneNumber,email]
        return newPartner

    def addToFamily():
        valid=False
        while valid==False:
            print(bcolors.OKCYAN+"Introduzca el DNI del socio al que vamos a añadirle un familiar"+bcolors.ENDC)
            dni=input()
            if Checker.checkDNI(dni):
                valid=True
            else:
                print(bcolors.FAIL+"Introduzca un DNI existente!"+bcolors.ENDC)
        valid=False
        while valid==False:
            print(bcolors.OKCYAN+"Introduzca el familiar a añadir"+bcolors.ENDC)
            familyDNI=input()
            if Checker.checkDNI(familyDNI):
                if familyDNI==dni:
                    print(bcolors.FAIL+"Introduzca un DNI distinto!"+bcolors.ENDC)
                else:
                    valid=True
            else:
                print(bcolors.FAIL+"Introduzca un DNI existente!"+bcolors.ENDC)
        valid=False
        while valid==False:
            print(bcolors.OKCYAN+"Introduzca el tipo de familiar")
            print("1. Hijo")
            print("2. Padre")
            print("3. Pareja"+bcolors.ENDC)
            familytype=input()
            if familytype == "1" or familytype == "2" or familytype == "3":
                valid=True
            else:
                print(bcolors.FAIL+"Introduzca un numero valido"+bcolors.ENDC)
        data=[dni,familyDNI,familytype]
        return data

    def askForYearFees():
        print(bcolors.OKCYAN+"Introduzca el año que desea ver del control de cuotas:"+bcolors.ENDC)
        year=input()
        return year
    def addEvent():
        valid=False
        while(valid==False):
            print(bcolors.OKCYAN+"Introduzca una fecha para el evento (dd/mm/yyyy):"+bcolors.ENDC)
            eventDate = input()
            try:
                date1 = time.strptime(eventDate, '%d/%m/%Y')
                valid=True
            except ValueError:
                print(bcolors.FAIL+'¡Fecha no valida!'+bcolors.ENDC)
        #------------------------------------------#
        valid=False
        while(valid==False):
            print(bcolors.OKCYAN+"Introduze la fecha maxima de inscripcion (dd/mm/yyyy):"+bcolors.ENDC)
            maxDateInscription=input()
            try:
                date2 = time.strptime(maxDateInscription, '%d/%m/%Y')
                if(date1>date2):
                    valid=True
                else:
                    print(bcolors.FAIL+"La fecha maxima de inscripcion debe de ser menor a la del propio evento"+bcolors.ENDC)
            except ValueError:
                print(bcolors.FAIL+'¡Fecha no valida!'+bcolors.ENDC)
            
        print(bcolors.OKCYAN+"Introduzca la ciudad en la que se organiza el evento:"+bcolors.ENDC)
        city=input()
        print(bcolors.OKCYAN+"Introduzca la provincia de ciudad indicada:"+bcolors.ENDC)
        province=input()
        valid=False
        while(valid==False):
            print(bcolors.OKCYAN+"Introduzca el DNI del socio que organiza el evento:"+bcolors.ENDC)
            organizer=input()
            if(Checker.checkDNI(organizer)):
                if Checker.checkEventDay(eventDate,organizer)==False:
                    valid=True
                else:
                    print(bcolors.FAIL+"Este organizador ya tiene a su cargo un evento"+bcolors.ENDC)   
            else:
                print(bcolors.FAIL+"Este dni no se corresponde a ningun socio"+bcolors.ENDC)
            
        print(bcolors.OKCYAN+"Introduce los kilometros que durara la ruta:"+bcolors.ENDC)
        totalKM=input()
        print(bcolors.OKCYAN+"Introduce el precio necesario para asistir al evento:"+bcolors.ENDC)
        price=input()
        
        data=[eventDate,maxDateInscription,city,province,organizer,totalKM,price]
        return data

    