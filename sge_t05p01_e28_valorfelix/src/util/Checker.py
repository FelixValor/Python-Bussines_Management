from src.util.JsonHandler import JsonHandler
from src.modelo.Club import Club
from datetime import date
import datetime
import os
import re

class Checker:

    def checkFiles():
        if(os.path.isfile('datos/user.json')and os.path.isfile('datos/partner.json')):
            pass
        else:
            diccUser=[{"DNI": "11111111K","password": "admin","lastAccesss": None,"isAdmin": True}]
            diccPartner=[{"fullname": None,"address": None,"phoneNumber": None,"email": None,"listBikes": None,"family": None}]
            JsonHandler.createJSON(diccUser, "datos/user.json")
            JsonHandler.createJSON(diccPartner, "datos/partner.json")


    def checkIsAdmin(dni):
        correct=False
        partners=JsonHandler.readJSON("datos/user.json")
        for x in partners:
            checkDNI=(x["DNI"])
            if checkDNI==dni:
                checkAdmin=(x["isAdmin"])
                if checkAdmin:
                    correct=True
                break
        return correct

    def checkDNI(dni):
        correct=False
        partners=JsonHandler.readJSON("datos/user.json")
        for x in partners:
            checkDNI=(x["DNI"])
            if checkDNI==dni:
                correct=True
                break
        return correct
    
    def checkPassword(dni,password):
        correct=False
        partners=JsonHandler.readJSON("datos/user.json")
        for x in partners:
            checkDNI=(x["DNI"])
            if checkDNI==dni:
                checkPassword=(x["password"])
                if checkPassword==password:
                    correct=True
                    break
        return correct

    def checkEventDay(date,dni):
        correct=False
        events=JsonHandler.readJSON("datos/events.json")
        for x in events:
            if x["organizer"]==dni:
                if x["eventDate"]==date:
                    correct=True
        return correct

    def isValidEmail(email):
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        return re.match(expresion_regular, email) is not None

    def verifyDNI(nif):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        numeros = "1234567890"
        respuesta=False
        if (len(nif) == 9):
            letraControl = nif[8].upper()
            dni = nif[:8]
            if ( len(dni) == len( [n for n in dni if n in numeros] ) ):
                if tabla[int(dni)%23] == letraControl:
                    respuesta=True
        return respuesta
        
    def verifyPhone(phone):
        regex = r"^([\d]{1,5})\s?([\d][\s\.-]?){6,7}$"    
        result = re.match(regex, phone)      
        if result is None:
            return False      
        return True
    
    def userHasPaid(dni):
        year=date.today().year
        fees=JsonHandler.readJSON("datos/fees.json")
        users=JsonHandler.readJSON("datos/user.json")

        
        hasPaid=fees.get(str(year))[Club.whereIsDNI(dni)-1][dni]["isPayed"]
        lastAccess=users[Club.whereIsDNI(dni)]["lastAccesss"]
        lastAccess=datetime.datetime.strptime(lastAccess,"%d/%m/%Y")
        thirtyDaysAgo = datetime.datetime.now() - datetime.timedelta(30)
        thirtyDaysAgo = datetime.datetime.strftime(thirtyDaysAgo,"%d/%m/%Y")
        thirtyDaysAgo = datetime.datetime.strptime(thirtyDaysAgo,"%d/%m/%Y")

        print("hace 30 dias:",thirtyDaysAgo.strftime("%d/%m/%Y"))
        print("ultimoAcceso: ",lastAccess)
        if hasPaid==False and thirtyDaysAgo>lastAccess:
            return False
        return True