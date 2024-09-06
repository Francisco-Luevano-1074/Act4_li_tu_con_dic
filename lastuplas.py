arcoiris=("Azul","Verde","Rojo","Amarillo")
print(arcoiris)
print("--Longitud arcoiris--")
print(len(arcoiris))
animales=("pantera",20,"estatura",1.7)
print(animales)
print("elementos de la tupla")
print(animales[2])
ratero = ("Juan", "Ana", "Pedro")
y = list(ratero)
y[1] = "Polainas"
x = tuple(y)
print(x)
print("Agregando elementos")
Nanimal=("Boby","Chetos")
y=list(Nanimal)
print(y)
y.append("Tontolín")
otratupla = tuple(y)
print(otratupla)
print("Uso de for en tuplas")
for elcolor in arcoiris:
    print(elcolor)



