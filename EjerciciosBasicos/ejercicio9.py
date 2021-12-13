vocales=("a","e","i","o","u")
b=True
contadorVocales=0
contadorConsonantes=0
contadorOtrosSignos=0
while(b):
    esConsonante=True
    print("Introduce un caracter")
    caracter=input()
    if(caracter != " "):
        if(caracter.isalpha()):
            print("entra")
            for x in vocales:
                if(caracter==x):
                    contadorVocales=contadorVocales+1
                    esConsonante=False
                    break
            if(esConsonante):
                contadorConsonantes=contadorConsonantes+1
        else:
            contadorOtrosSignos=contadorOtrosSignos+1
    else:
        b=False

print("Vocales:",contadorVocales)
print("Consonates:",contadorConsonantes)
print("OtrosSignosa:",contadorOtrosSignos)
print("Caracteres totales:",contadorVocales+contadorConsonantes+contadorOtrosSignos)




