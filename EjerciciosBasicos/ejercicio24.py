import os
import json
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

menu=True
contador_dicc=1
dicc_clientes={}
esPreferente=True
while menu:
    
    print("(1) Añadir cliente")
    print("(2) Eliminar cliente")
    print("(3) Mostrar cliente")
    print("(4) Listar todos los clientes")
    print("(5) Listar clientes preferentes")
    print("(6) Ordenar por apellidos. ")
    print("(7) Terminar. ")
    orden=input()
    
    match orden:
        case "1":
            clear()
            print("Introduzca los siguientes campos")
            print("NIF:")
            nif=input()
            print("Nombre:")
            nombre=input()
            print("Apellidos:")
            apellidos=input()
            print("Direccion:")
            direccion=input()
            print("Telefono:")
            telefono=input()
            print("Correo:")
            correo=input()
            print("¿Es preferente? (s/n)")
            preferente=input()
            if(preferente!="s"):
                esPreferente=False

            datos=[nombre,apellidos,direccion,telefono,correo,esPreferente]
            dicc_clientes[nif]=datos

            contador_dicc=contador_dicc+1
        case "2":
            clear()
            print("Introduza el DNI del cliente a eliminar")
            nifABorrar=input()
            del dicc_clientes[nifABorrar]
            print("Se ha borrado el cliente con nif",nifABorrar)
        case "3":
            clear()
            print("Introduzca el DNI del cliente a mostrar")
            nifAMostrar=input()
            print(json.dumps(dicc_clientes[nifAMostrar],indent=4))
        case "4":
            clear()
            print("Listado de todos los clientes:")
            print(json.dumps(dicc_clientes,indent=4))
        case "5":
            clear()
            print("Listado de los clientes preferentes:")
            listaPreferentes=[]
            for x in dicc_clientes.keys():
                if(dicc_clientes[x][5]==True):
                    listaPreferentes=listaPreferentes+[x+" "+dicc_clientes[x][0]+" "+dicc_clientes[x][1]]
            print(listaPreferentes)
        case "6":
            clear()
            print("Listado de todos los clientes ordenado por apellidos:")
            listaOrdenada=sorted(dicc_clientes.items(),key=lambda item:item[1])
            print(json.dumps(listaOrdenada,indent=4))
        case "7":
            clear()
            print("Fin del programa")
            menu=False



