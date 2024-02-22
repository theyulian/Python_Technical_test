#Numero y repeticiones a sumar

def calcular(numero, termino):
    suma = 0
    numero_str = str(numero)
    for i in range(1, termino + 1):
        num_repeticiones = int(numero_str * i)
        suma += num_repeticiones
        print(f"{numero_str * i}", end="")
        if i < termino:
            print(" + ", end="")
        else:
            print()
    print("Resultado: ", suma)

if __name__ == "__main__":
    numero = int(input("Introduce el número base: "))
    termino = int(input("Introduce el término: "))
    calcular(numero, termino)
