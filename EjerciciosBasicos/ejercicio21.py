print("Introduce el numero de digitos para rellenar las listas")
tamannoLista=int(input())

lista1=[]
lista2=[]

for i in range(tamannoLista):
    print("Introduzca un numero para la lista1:")
    valorLista=input()
    lista1.append(valorLista)

for i in range(tamannoLista):
    print("Introduzca un numero para la lista2:")
    valorLista=input()
    lista2.append(valorLista)

print("Lista 1:",lista1)
print("Lista 2:",lista2)

try:
    lista3=lista1*2
    print("Lista 3:",lista3)
except:
    print("No se puede realizar esta operacion")

try:
    lista4=lista1*+3
    print("Lista 4:",lista4)
except:
    print("No se puede realizar esta operacion")

try:
    lista5=lista1*lista2
    print("Lista 5:",lista5)
except:
    print("No se puede realizar esta operacion")

try:
    lista6=lista1+lista2
    print("Lista 6:",lista6)
except:
    print("No se puede realizar esta operacion")

try:
    lista7=lista1
    print("Lista 7:",lista7)
except:
    print("No se puede realizar esta operacion")

lista1_set=set(lista1)
lista8=list(lista1_set.intersection(lista2))

print("Lista 8:",lista8)
print("Tamaño de la lista 8:",len(lista8))
