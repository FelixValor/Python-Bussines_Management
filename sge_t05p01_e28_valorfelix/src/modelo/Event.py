class Event:
    def __init__(self,eventDate,maxDateInscription,city,province,organizer,totalKM,price,partnerListClub):
        self._eventDate=eventDate
        self._maxDateInscription=maxDateInscription
        self._city=city
        self._province=province
        self._organizer=organizer
        self._totalKM=totalKM
        self._price=price
        self._partnerListClub=partnerListClub
        
    def parseEventToJSON(self):
        dicc={"eventDate":self._eventDate,"maxDateInscription":self._maxDateInscription,
            "city":self._city,"province":self._province,"organizer":self._organizer,
            "totalKM":self._totalKM,"price":self._price,"partnerListClub":self._partnerListClub}
        return dicc