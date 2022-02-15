from src.util.JsonHandler import JsonHandler
import os

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
