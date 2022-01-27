from enum import Enum
class Category(Enum):
    RUEDAS="Ruedas"
    FRENOS="Frenos"
    ASIENTO="Asiento"
    CUADRO="Cuadro"
    MANILLAR="Manillar"
    PLATOS="Platos"
    OTROS="Otros"

class Repair:
    def __init__(self,date,cost,description,category: Category):
        self._date=date
        self._cost=cost
        self._description=description
        self._category=category
        