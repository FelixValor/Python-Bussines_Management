from src.modelo.Partner import Partner, User
from src.utilidades.JsonHandler import JsonHandler
from src.vista import menuAdministracion
import os
def clear():
    a=1
    
class AdminController:
    
    def startMenu():
        menu = True
        while menu:
            
            orden=menuAdministracion.showMenu()
            match orden:
                case "1":
                    clear()
                    menuAdministracion.printConsole("---Socios---")
                    menuAdministracion.showPartners(JsonHandler.readJSON("datos/partner.json"))
                case "2":
                    clear()
                    newPartner=menuAdministracion.askForNewPartner()
                    JsonHandler.writeJSON(Partner.parsePartnerToJSON(Partner(newPartner._partner._fullName,newPartner._partner._address,newPartner._partner._phoneNumber,newPartner._partner._email)),"datos/partner.json") 
                    JsonHandler.writeJSON(User.parseUserToJSON(User(newPartner._dni,newPartner._password,newPartner._isAdmin,newPartner._isAdmin,None,None,None,None)),"datos/user.json")
                case "3":
                    clear()
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


