import json
class JsonHandler:

    def readJSON(fileName):
        fp=open(fileName,"r")
        fileData=json.load(fp)
        fp.close()
        return fileData