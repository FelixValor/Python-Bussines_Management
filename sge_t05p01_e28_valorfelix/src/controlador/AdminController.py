from re import A
from src.modelo.Partner import Partner, User
from src.util.JsonHandler import JsonHandler
from src.vista.AdminMenu import AdminMenu
import os
def clear():
    a=1
    
class AdminController:

    def __init__(self):
        pass

    def startMenu(self):
        menu = True
        while menu:
            
            orden=AdminMenu.showMenu()
            match orden:
                case "1":
                    clear()
                    AdminMenu.printConsole("---Socios---")
                    self.showPartners(JsonHandler.readJSON("datos/partner.json"))
                case "2":
                    clear()
                    p=AdminMenu.askForNewPartner()
                    newPartner=User(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7])
                    """if(self.verifyDNI(newPartner._dni)):
                        JsonHandler.writeJSON(Partner.parsePartnerToJSON(Partner(newPartner._partner._fullName,newPartner._partner._address,newPartner._partner._phoneNumber,newPartner._partner._email)),"datos/partner.json") 
                        JsonHandler.writeJSON(User.parseUserToJSON(User(newPartner._dni,newPartner._password,newPartner._isAdmin,newPartner._isAdmin,None,None,None,None)),"datos/user.json")
                        print("bien")
                    else:
                        print("mal")"""
                    JsonHandler.writeJSON(Partner.parsePartnerToJSON(Partner(newPartner._partner._fullName,newPartner._partner._address,newPartner._partner._phoneNumber,newPartner._partner._email)),"datos/partner.json") 
                    JsonHandler.writeJSON(User.parseUserToJSON(User(newPartner._dni,newPartner._password,newPartner._isAdmin,newPartner._isAdmin,None,None,None,None)),"datos/user.json")
                case "3":
                    clear()
                    data=AdminMenu.addToFamily()
                    users=JsonHandler.readJSON("datos/user.json")
                    dni1=0
                    dni2=0
                    posicion=0
                    for x in users:
                        if(x["DNI"]==data[0]):
                            dni1=x["DNI"]
                            dniLocation=posicion
                        if(x["DNI"]==data[1]):
                            dni2=x["DNI"]
                        posicion=posicion+1
                    
                    if(dni1!=dni2 and dni1!=0 and dni2!=0):
                        print(dni1,"--->",dni2)
                        familiar=""
                        if(data[2]=="1"):
                            familiar="hijo"
                        elif(data[2]=="2"):
                            familiar="pareja"
                        elif(data[2]=="3"):
                            familiar="padre"
                        JsonHandler.insertFamilyInJSON(dniLocation,dni2)
                    else:
                        print("mal")
                case "4":
                    clear()
                    
                case "5":
                    clear()
                case "6":
                    clear()
                case "7":
                    clear()
                case "8":
                    clear()
                case "9":
                    clear()
                case "0":
                    print("Programa finalizado")
                    menu=False
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

    def showPartners(self,partners:dict):
        for x in partners:
            AdminMenu.printConsole(x["fullname"])




