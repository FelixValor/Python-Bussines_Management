class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def _str_(self):
        return  "({}, {})".format(self.x, self.y)
    
    
    def cuadrante(self):
        if self.x==0 and self.y==0:
            print ('Origen')
        if self.x==0:
            print ('Eje Y')
        if self.y==0:
            print ('Eje X')
        if self.x>0 and self.y>0:
            print ('Cuadrante 1')
        if self.x<0 and self.y>0:
            print ('Cuadrante 2')
        if self.x<0 and self.y<0:
            print ('Cuadrante 3')
        if self.x>0 and self.y<0:
            print ('Cuadrante 4')
    
    def vector(self,p):
        print("El vector entre {} y {} es ({}, {})".format(
            self, p, p.x - self.x, p.y - self.y))

class Rectangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

menu=True
print("Introduzca el primer punto:")
p1=input()
print("Introduzca el segundo punto:")
p2=input()
p = Punto(int(p1),int(p2))
while menu:
    print("1 Operaciones con puntos:")
    print("2 Operaciones con rectangulos:")
    print("3 Salir")
    orden=input()
    match orden:
        case "1":
            print("a. Mostrar cuadrante al que pertenecen")
            print("b. Calcular vector")
            print("c. Calcular distancia")
            orden=input()
            match orden:
                case "a":
                    p.cuadrante()
                case "b":
                    print("Introduzca un nuevo punto")
                    print("primer punto:")
                    p1Vector=input()
                    print("segundo punto:")
                    p2Vector=input()
                    pVector=Punto(int(p1Vector),int(p2Vector))
                    p.vector(pVector)
        case "2":
            print("a. Calcular base")
            print("b. Calcular altura")
            print("c. Calcular area")
        case "3":
            print("fin del programa")
            menu=False