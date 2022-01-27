import json
from src.modelo.Partner import User
class Prueba:

    def ejecutaPrueba():
        """user1=User("11111111K","1234","12/10/2021",True,"Felix Valor","Calle Castellanos 136","6099767963","valorfelix@gmail.com")
        d1=user1._partner.parsePartnerToJSON()
        d=User.parseUserToJSON(user1)
        fp=open('user.json','w')
        fp1=open('partner.json','w')
        json.dump([d],fp)
        json.dump([d1],fp1)
        fp.close()"""
        Prueba.readJSON("datos/user.json")
    

    def readJSON(fileName):
        fp=open(fileName,"r")
        ret=json.load(fp)
        print (ret)
        fp.close()

        
