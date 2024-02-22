#Filtrar elementos

def filtrar_numeros(lista):
    salida = []
    for num in lista:
        if num > 1000:
            return salida
        if num <= 600 and num % 5 == 0:
            salida.append(num)
    return salida

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
    
    resultado = filtrar_numeros(entrada)
    print("Números filtrados:", resultado)
