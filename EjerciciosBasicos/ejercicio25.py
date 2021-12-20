class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return self.x+","+self.y
    
    
    def cuadrante(self):
        if(self.x==0&self.y!=0):
            print("1º cuadrante")
        if(self.x!=0&self.y==0):
            print("2º cuadrante")
        if(self.x==0&self.y!=0):
            print("3º cuadrante")
        if(self.x==0&self.y!=0):
            print("4º cuadrante")
            

class Rectangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

menu=True
while menu:
    print("1 Operaciones con puntos:")
    print("2 Operaciones con rectangulos:")
    print("3 Salir")
    orden=input()
    match orden:
        case 1:
            print("a. Mostrar cuadrante al que pertenecen")
            print("b. Calcular vector")
            print("c. Calcular distancia")
            