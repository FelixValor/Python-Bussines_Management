import json

from src.modelo.Partner import Partner
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
            json.dump(data, file)