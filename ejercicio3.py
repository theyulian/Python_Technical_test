#Organizar elementos

def agrupar_elementos_similares(lista):
    grupos = {}
    for elemento in lista:
        if elemento in grupos:
            grupos[elemento].append(elemento)
        else:
            grupos[elemento] = [elemento]
    return list(grupos.values())

if __name__ == "__main__":
    entrada = []
    print("A continuación digita los números que desees en la lista de entrada uno a uno.")
    print("La lista tiene una longitud indefinida, para terminar escribe una letra cualquiera")
    while True:
        try:
            num = int(input("Introduce un número para agregar (o cualquier letra para finalizar): "))
            entrada.append(num)
        except ValueError:
            break
    
    resultado = agrupar_elementos_similares(entrada)
    print("Resultado:", resultado)
