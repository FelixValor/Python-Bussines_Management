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
                    menuAdministracion.showPartners(JsonHandler.readJSON("datos/partner.json"))
                case "2":
                    clear()
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


