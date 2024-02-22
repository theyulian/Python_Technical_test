This is a basic test using python language

To compile these exercises you need to download python,
in my case I used version 3.12.2. I did the entire process from VSCode,
but you can feel free to use any other terminal using, for example, the command "py exercise1.py"

Ejercicio 1: 

    Escriba una función que retorne la suma de una serie de X número repetido hasta el n-ésimo término. Ejemplos: 
    Entrada : numero=3, terminos=5 
    Salida : 37035 #(3 + 33 + 333 + 3333 + 33333) 
    
    Se le pide primeramente dos datos al usuario, el numero base y la cantidad de repeticiones. Posterior a ello se llama a una función calcular
    , la cual convierte el numero base a string y realiza el debido proceso para adjuntarlo entre sí y sumarlo cuantas veces sea solicitado. 

Ejercicio 2: 

    Escriba una función que retorne en una lista de salida, solo aquellos números de una lista de entrada que satisfagan las 
    siguientes condiciones: 
    1. El número debe ser divisible por cinco. 
    2. Si el número es mayor que 600, no se incluye en la salida. 
    3. Si el número es mayor que 1000, detenga el procesamiento y retorne el resultado. 
    
    En este caso primero se le solicita al usuario agregar cada uno de los números que van a conformar la lista de entrada, 
    adjuntándolos de uno en uno con una longitud indefinida. Luego de ello llama a la función filtrar_numeros para realizar 
    los correspondientes filtros y finalmente imprimir la lista final. 

Ejercicio 3: 

    Dada una lista de cualquier longitud de entrada, escriba una función para agrupar los elementos similares en una matriz 
    de salida (no importa el orden). Ejemplos: 
    Entrada : list = [12, 25, 1, 1, 7, 25] 
    Salida : [[12], [7], [25, 25], [1, 1]] 
    
    De igual forma al ejercicio anterior, se le solicita una lista de números de tamaño indefinido al usuario. Luego de ello, 
    mediante la función agrupar_elementos_similares se crea un diccionario que comprueba cada elemento de la lista inicial y lo 
    compara con sí mismo, decidiendo así si solo debe adjuntarlo a un campo ya creado o si se necesita crear uno nuevo. 

Ejercicio 4. 

    Se tiene un menú de manejo de inventarios con 3 opciones: La primera es agregar un nuevo producto, donde a través de una función 
    se le solicita al usuario el grupo, el nombre y la cantidad de dicho producto, para confirmar su existencia y añadirlo al inventario
    según como corresponda; La segunda opción es mostrar inventarios, donde se llama a una función diferente a la primera y de manera organizada
    imprime las tres categorías y los productos correspondientes a cada una de ellas con sus cantidades; Y finalmente se tiene la opción salir, 
    donde el programa se cierra.  
    
    Para este ejercicio quiero resaltar dos cosas, la primera es que se eligió un stock inicial de 3 productos en cada una de las 3 categorías,
    y la segunda es que vi de utilidad agregar la confirmación de minúsculas y mayúsculas a las entradas que el usuario envía, de este modo sin 
    importar si el usuario escribe “RICE” o “rice”, el producto irá a la misma categoría. 
