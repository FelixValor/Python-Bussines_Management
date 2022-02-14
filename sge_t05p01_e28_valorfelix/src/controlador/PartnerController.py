
import imp
from src.vista.PartnerMenu import PartnerMenu

class PartnerController:

    def startMenu(self):
        menu = True
        while menu:
            
            orden=PartnerMenu.showMenu()
            match orden:
                case "1":
                    print("A")
                case "2":
                    print("A")
                case "3":
                    print("A")
                case "4":
                    print("A")
                case "5":
                    print("A")
                case "6":
                    print("A")
                case "7":
                    print("A")
                case "8":
                    print("A")
                case "9":
                    print("A")
                case "0":
                    print("Programa finalizado")
                    menu=False