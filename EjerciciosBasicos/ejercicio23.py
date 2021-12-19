import json
abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Introduzca una cadena:")
"""Controlamos que todo sean minusculas"""
cadena=input().lower()
if(cadena!=""):
    """Controlamos que siempre haya solo un espacio entre cada palabra"""
    cadena=" ".join(cadena.split())
    """Creamos una lista con todas las palabras"""
    listaPalabras=cadena.split(' ')
    """Para el diccionario de letras no necesitaremos los espacios asi que los quitaremos"""
    listaLetras=list(cadena.replace(" ",""))
    """Creamos el diccionario de palabras """
    dicc_pal={i:listaPalabras.count(i) for i in listaPalabras}
    print("DICCIONARIO DE PALABRAS")
    print(json.dumps(dicc_pal,indent=4))
    """Creamos el diccionario de letras"""
    dicc_let={i:listaLetras.count(i) for i in abecedario}
    print("DICCIONARIO DE LETRAS")
    print(json.dumps(dicc_let,indent=4))
else:
    print("No dejes la cadena vacia")





