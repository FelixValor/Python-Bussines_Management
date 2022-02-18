from turtle import position
from src.util.JsonHandler import JsonHandler
class Club:
    def __init__(self, name, CIF):
        self._name=name
        self._CIF=CIF
        self._headquarters=None
        self._listPartners=None
        self._listEvents=None
        self._totalBalance=None
    
    def listarSocios(self):
        
        return self._listPartners


    def whoIsDNI(dni):
        position=0
        partners=JsonHandler.readJSON("datos/partner.json")
        users=JsonHandler.readJSON("datos/user.json")
        fullname=""
        for x in users:
            if dni==x["DNI"]:
                fullname=partners[position]["fullname"]
            position=position+1
        return fullname

    def whereIsDNI(dni):
        i=0
        users=JsonHandler.readJSON("datos/user.json")
        for x in users:
            if dni==x["DNI"]:
                position=i
            i=i+1
        return position