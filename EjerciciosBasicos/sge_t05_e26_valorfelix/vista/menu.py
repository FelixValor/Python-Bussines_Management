import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

menu = True

while menu:
    
    print("(1) Nuevo cliente y saldo de partida ")
    print("(2) Buscar y mostrar una cuenta por dni o por número")
    print("(3) Buscar cuentas con un saldo superior a una cantidad dada")
    print("(4) Añadir un movimiento a una cuenta por dni")
    print("(5) Mostrar información completa del Banco")
    print("(6) Salir.")
    orden=input()

    match orden:
        case "1":
            clear()
        case "2":
            clear()
        case "3":
            clear()
        case "4":
            clear()
        case "5":
            clear()
        case "6":
            print("Programa finalizado")
            menu=False