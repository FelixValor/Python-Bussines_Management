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