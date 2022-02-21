from src.util.JsonHandler import JsonHandler
from src.vista.PartnerMenu import PartnerMenu
from src.modelo.Event import Event
from src.modelo.Club import Club

class PartnerController:

    def __init__(self,userLogged):
        self.userLogged=userLogged
        

    def startMenu(self):
        menu = True
        while menu:
            
            orden=PartnerMenu.showMenu()
            match orden:
                case "1":
                    print("A")
                case "2":
                    dicc=JsonHandler.readJSON("datos/events.json")
                    PartnerController.showEvents(dicc)
                    PartnerController.askForJoinningEvent(self.userLogged,dicc)
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
    def showEvents(events):
        count=0
        for x in events:
            count=count+1
            PartnerMenu.printConsole("Evento:"+str(count))
            PartnerMenu.printConsole(Event(x["eventDate"],x["maxDateInscription"],
            x["city"],x["province"],x["organizer"],x["totalKM"],x["price"],x["partnerList"]))
            PartnerMenu.printConsole("-------------------------------------------------")

    def askForJoinningEvent(dniLogged,events):
        count=0
        for x in events:
            count=count+1
        idEvent=PartnerMenu.askIfJoin(count)
        if idEvent != -1:
            dicc=events
            if dicc[int(idEvent)-1]["partnerList"] == None:
                dicc[int(idEvent)-1]["partnerList"]=[dniLogged]
            else:
                correct=True
                for p in dicc[int(idEvent)-1]["partnerList"]:
                    if p==dniLogged:
                        correct=False
                        PartnerMenu.printErrorConsole("Ya estas dentro de este evento")
                        break
                
                if correct:
                    dicc[int(idEvent)-1]["partnerList"].append(dniLogged)
            JsonHandler.createJSON(dicc,"datos/events.json")
            
            