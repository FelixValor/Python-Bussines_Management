from src.util.JsonHandler import JsonHandler


class StartChecker:
    def checkIsAdmin(dni):
        correct=False
        partners=JsonHandler.readJSON("datos/user.json")
        for x in partners:
            checkDNI=(x["DNI"])
            if checkDNI==dni:
                checkAdmin=(x["isAdmin"])
                if checkAdmin:
                    correct=True
                break
        return correct

    def checkDNILogin(dni):
        correct=False
        partners=JsonHandler.readJSON("datos/user.json")
        for x in partners:
            checkDNI=(x["DNI"])
            if checkDNI==dni:
                correct=True
                break
        return correct
    
    def checkPassord(dni,password):
        correct=False
        partners=JsonHandler.readJSON("datos/user.json")
        for x in partners:
            checkDNI=(x["DNI"])
            if checkDNI==dni:
                checkPassword=(x["password"])
                if checkPassword==password:
                    correct=True
                    break
        return correct