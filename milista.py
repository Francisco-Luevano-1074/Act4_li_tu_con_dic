# ejemplo de uso de listas
misnovios=["Chambajal","Larrondo","Emi"]
misnumeros=["666","77","21"]
# Mostrando mis novios
print(misnovios)
# Mostrando mis números raros
print(misnumeros)
print("---accediendo a los elementos de la lista---")
print(misnovios[-2])
if "Montelongo" in misnovios:
    print("Sí, 'Montelongo' está en la lista de mis novios")
else:
    print("Chale, no es mi novio")
    print("Número de novios")
    Nnovias=len(misnovios)
    print(f"Número de novios = {Nnovias}")
    print("Ciclo for en listas")
    posicion=0
    for medianaranja in misnovios:
        print(posicion," ",medianaranja)
        posicion=posicion+1