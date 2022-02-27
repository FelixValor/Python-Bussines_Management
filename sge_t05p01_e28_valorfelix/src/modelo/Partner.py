
class Partner:
    def __init__(self, fullName, address, phoneNumber,email):
        self._fullName=fullName
        self._address=address
        self._phoneNumber=phoneNumber
        self._email=email
        self._listBikes=None
        self._family={"children":[],"fathers":[],"couple":""}


    def parsePartnerToJSON(self):
        dicc={"fullname":self._fullName,"address":self._address,"phoneNumber":self._phoneNumber,
                "email":self._email,"listBikes":self._listBikes,"family":self._family}
        return dicc

    

class User:
    def __init__(self, dni,password,lastAccess,isAdmin,fullname,address,phoneNumber,email):
        self._partner=Partner(fullname,address,phoneNumber,email)
        self._dni=dni
        self._password=password
        self._lastAccess=None
        self._isAdmin=isAdmin

#contemmplar aqui si el cliente esta al corriente del pago
    def parseUserToJSON(self):
        dicc={"DNI":self._dni,"password":self._password,"lastAccesss":self._lastAccess,"isAdmin":self._isAdmin}
        return dicc
