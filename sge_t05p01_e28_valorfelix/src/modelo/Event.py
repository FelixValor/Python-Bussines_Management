
from src.util.JsonHandler import JsonHandler
from src.modelo.Club import Club


class Event:
    def __init__(self,eventDate,maxDateInscription,city,province,organizer,totalKM,price,partnerList):
        self.eventDate=eventDate
        self.maxDateInscription=maxDateInscription
        self.city=city
        self.province=province
        self.organizer=organizer
        self.totalKM=totalKM
        self.price=price
        self.partnerList=partnerList
        
    def parseEventToJSON(self):
        dicc={"eventDate":self.eventDate,"maxDateInscription":self.maxDateInscription,
            "city":self.city,"province":self.province,"organizer":self.organizer,
            "totalKM":self.totalKM,"price":self.price,"partnerListClub":self.partnerList}
        return dicc

    def __str__(self):
        data=f"Organizador: {self.organizer}\nFecha: {self.eventDate}\nFecha Maxima Inscripcion: {self.maxDateInscription}\nCiudad: {self.city}\nProvincia:{self.province}\nLongitud: {self.totalKM}KM\nPrecio: {self.price}€\nSocios Apuntados:\n"
        if(self.partnerList == None): 
            data = data+"Nadie"
        else: 
            partners=JsonHandler.readJSON("datos/partner.json")
            users=JsonHandler.readJSON("datos/user.json")
            for partner in self.partnerList:
                """for u in users:
                    if partner==u["DNI"]:
                        count=count+1
                        fullname=partners[count]["fullname"]"""
                fullname=Club.whoIsDNI(partner)
                data = data+fullname+'\n'
                
        return data