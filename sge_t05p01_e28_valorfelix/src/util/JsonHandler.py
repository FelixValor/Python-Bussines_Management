import json


class JsonHandler:



    def readJSON(fileName):
        fp=open(fileName,"r")
        fileData=json.load(fp)
        fp.close()
        return fileData


    def writeJSON(d:dict,filename):
        with open(filename, "r+") as file:
            data = json.load(file)
            data.append(d)
            file.seek(0)
            json.dump(data, file,indent=4)

    def insertFamilyInJSON(locationDNI,dniToAdd):
            data=JsonHandler.readJSON("datos/partner.json")
            data[locationDNI]["family"]=[dniToAdd]
            print(data[locationDNI])