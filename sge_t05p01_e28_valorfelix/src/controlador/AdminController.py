from calendar import month
from turtle import position
from src.modelo.Club import Club
from src.modelo.Partner import Partner, User
from src.modelo.Event import Event
from src.util.JsonHandler import JsonHandler
from src.vista.AdminMenu import AdminMenu
import datetime
from datetime import date

import os
def clear():
    pass
    
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
                    print(newPartner._isAdmin)
                    JsonHandler.writeJSON(Partner.parsePartnerToJSON(Partner(newPartner._partner._fullName,newPartner._partner._address,newPartner._partner._phoneNumber,newPartner._partner._email)),"datos/partner.json") 
                    JsonHandler.writeJSON(User.parseUserToJSON(User(newPartner._dni,newPartner._password,newPartner._lastAccess,newPartner._isAdmin,None,None,None,None)),"datos/user.json")

                    year=date.today().year
                    month=date.today().month
                    price=0
                    if month <= 6:
                        price=15
                    else:
                        price=8
                    fees=JsonHandler.readJSON("datos/fees.json")
                    feesOfActualYear=fees.get(str(year))
                    feesOfActualYear.append({newPartner._dni:{"payday":"","isPayed":False,"price":price,"discount":0}})
                    
                    fees[str(year)]=feesOfActualYear
                    JsonHandler.createJSON(fees,"datos/fees.json")
                    
                    
                case "3":
                    clear()
                    data=AdminMenu.addToFamily()
                    
                    dni1=data[0]
                    dni2=data[1]
                    familyType=data[2]
                    partners=JsonHandler.readJSON("datos/partner.json")
                    posDNI1=Club.whereIsDNI(dni1)
                    posDNI2=Club.whereIsDNI(dni2)
                    if familyType=="1":
                        if partners[posDNI1]["family"]["fathers"]==[]:
                            isAdded=False
                            isAddedAsFather=False
                            isAddedAsCouple=False
                            for x in partners[posDNI1]["family"]["children"]:
                                if x==dni2:
                                    isAdded=True
                                    break
                            for x in partners[posDNI1]["family"]["fathers"]:
                                if x==dni2:
                                    isAddedAsFather=True
                                    break
                            if partners[posDNI1]["family"]["couple"]==dni2:
                                isAddedAsCouple=True



                            if isAdded==False:
                                if isAddedAsFather:
                                    AdminMenu.printErrorConsole("No puedes insertar como hijo a un padre")
                                else:
                                    if isAddedAsCouple:
                                        AdminMenu.printErrorConsole("No puedes insertar como hijo a una pareja")
                                    else:
                                        partners[posDNI1]["family"]["children"].append(dni2)
                                        partners[posDNI2]["family"]["fathers"].append(dni1)
                                        JsonHandler.createJSON(partners,"datos/partner.json")
                                        self.applyFees()
                            else:
                                AdminMenu.printErrorConsole("No puedes insertar 2 veces el mismo hijo")
                        else:
                            AdminMenu.printErrorConsole("El socio ya esta integrado como hijo por lo que no puede tener hijos")
                    elif familyType=="2":
                        
                        isAdded=False
                        for x in partners[posDNI1]["family"]["fathers"]:
                            if x==dni2:
                                isAdded=True
                                break
                        isAddedAsChildren=False
                        for x in partners[posDNI1]["family"]["children"]:
                            if x==dni2:
                                isAddedAsChildren=True
                                break
                            
                        if isAdded==False:
                            if partners[posDNI2]["family"]["couple"]=="":
                                pass
                            else:
                                dniCouple=partners[posDNI2]["family"]["couple"]
                                position=Club.whereIsDNI(dniCouple)
                                partners[position]["family"]["children"].append(dni1)
                                partners[posDNI1]["family"]["fathers"].append(dniCouple)
                            partners[posDNI1]["family"]["fathers"].append(dni2)
                            partners[posDNI2]["family"]["children"].append(dni1)
                            JsonHandler.createJSON(partners,"datos/partner.json")
                            self.applyFees()
                        else:
                            AdminMenu.printErrorConsole("No puedes insertar 2 veces el mismo padre")
                    elif familyType=="3":
                        if partners[posDNI1]["family"]["fathers"]==[]:
                            if partners[posDNI1]["family"]["couple"]=="":
                                if partners[posDNI2]["family"]["couple"]=="":
                                    partners[posDNI1]["family"]["couple"]=dni2
                                    partners[posDNI2]["family"]["couple"]=dni1
                                    JsonHandler.createJSON(partners,"datos/partner.json")
                                    self.applyFees()
                                else:
                                    p=partners[posDNI2]["fullname"]
                                    couple=partners[posDNI2]["family"]["couple"]
                                    AdminMenu.printErrorConsole("El socio con dni "+dni2+"("+p+") ya tiene pareja ("+Club.whoIsDNI(couple)+")")
                            else:
                                p=partners[posDNI1]["fullname"]
                                couple=partners[posDNI1]["family"]["couple"]
                                AdminMenu.printErrorConsole("El socio con dni "+dni1+"("+p+") ya tiene pareja ("+Club.whoIsDNI(couple)+")")
                        else:
                            AdminMenu.printErrorConsole("El socio ya esta integrado como hijo por lo que no puede tener pareja")
                case "4":
                    clear()
                    today=datetime.datetime.today()
                    today=datetime.datetime.strftime(today,"%d/%m/%Y")
                    today=datetime.datetime.strptime(today,"%d/%m/%Y")
                    events=JsonHandler.readJSON("datos/events.json")
                    for x in events:
                        eventDate=x["eventDate"]
                        eventDate=datetime.datetime.strptime(eventDate,"%d/%m/%Y")
                        
                        if eventDate>=today:
                            AdminMenu.printConsole(Event(x["eventDate"],x["maxDateInscription"],
                            x["city"],x["province"],x["organizer"],x["totalKM"],x["price"],x["partnerList"]))
                case "5":
                    print("A")
                case "6":
                    e=AdminMenu.addEvent()
                    newEvent=Event(e[0],e[1],e[2],e[3],e[4],e[5],e[6],None)
                    if(os.path.isfile('datos/events.json')):
                        dicc=Event.parseEventToJSON(newEvent)
                        JsonHandler.writeJSON(dicc, "datos/events.json")
                    else:
                        dicc=[Event.parseEventToJSON(newEvent)]
                        JsonHandler.createJSON(dicc, "datos/events.json")
                case "7":
                    year=AdminMenu.askForYearFees()
                    fees=JsonHandler.readJSON("datos/fees.json")
                    users=JsonHandler.readJSON("datos/user.json")
                    selectedYearFees=fees.get(str(year))
                    usersDNIList=[]
                    for y in users:
                        usersDNIList.append(y["DNI"])
                    i=1
                    for x in selectedYearFees:
                        dni=usersDNIList[i]
                        price=x[dni]["price"]
                        discount=x[dni]["discount"]
                        if discount==0:
                            message=(Club.whoIsDNI(dni)+" tiene que pagar "+str(price))
                            AdminMenu.printConsole(message)
                        else:
                            finalPrice=price-(price*discount/100)
                            message=(Club.whoIsDNI(dni)+" tiene que pagar "+str(finalPrice))
                            AdminMenu.printConsole(message)
                        i=i+1
                case "8":
                    self.applyFees()
                case "9":
                    year=date.today().year
                    dni=AdminMenu.askForDNIToPay()
                    fees=JsonHandler.readJSON("datos/fees.json")
                    fees.get(str(year))[Club.whereIsDNI(dni)-1][dni]["isPayed"]=True
                    JsonHandler.createJSON(fees,"datos/fees.json")
                case "0":
                    print("Programa finalizado")
                    menu=False
    

    def showPartners(self,partners:dict):
        listOfNames=[]
        for x in partners:
            if(x["fullname"]==None):
                pass
            else:
                listOfNames.append(x["fullname"].lower())

        listOfNames.sort()
        for y in listOfNames:
            AdminMenu.printConsole(y)


    def applyFees(self):
        month=date.today().month
        year=date.today().year
        partners=JsonHandler.readJSON("datos/partner.json")
        users=JsonHandler.readJSON("datos/user.json")
        dniList=[]
        for x in users:
            pos=Club.whereIsDNI(x["DNI"])
            if pos==0:
                pass
            else:
                price=0
                if month <= 6:
                    price=15
                else:
                    price=8
                print(pos)
                discount=0
                
                if partners[pos]["family"]["children"]!=[] or partners[pos]["family"]["fathers"]!=[]:
                    discount=15
                if partners[pos]["family"]["couple"]!="":
                    discount=10
                if partners[pos]["family"]["couple"]!="" and partners[pos]["family"]["children"]!=[]:
                    discount=30

                dniList.append({x["DNI"]:{"payday":"","isPayed":False,"price":price,"discount":discount}})
        fees=JsonHandler.readJSON("datos/fees.json")
        fees[str(year)]=dniList 
        JsonHandler.createJSON(fees,"datos/fees.json")

