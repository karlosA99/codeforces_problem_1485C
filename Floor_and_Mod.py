import math
from random import randint

def CountSpecialsPairs_BF(x, y):
    count = 0  #inicializamos la cantidad de pares especiales en 0
     
    for i in range(1, x + 1):         #con estos dos ciclos for creamos todos los posibles pares (a,b)
        for j in range(1, y + 1):
            div = i // j
            mod = i % j
            if (div == mod):    #comprobamos si cumplen la propiedad de formar un par especial
                count += 1    #en caso positivo aumentamos count en 1
    return count
    

def CountSpecialsPairs_NT(x, y):
    count = 0
    
    for i in range(1, int(math.sqrt(x)) + 1):   #solo hacemos el ciclo hasta la raiza de x, los motivos estan bien explicado en el pdf
        count+= max(0,min(y, int(x/i) - 1) - i)   #aplicamos la fórmula obtenida luego de un trabajo matemático (bien explicado en el pdf)
    return count

def Tester(count_tests, ran_x, ran_y):

    results = []  #esta lista guarda en orden lo que dan los resultados
    incorrects = []  # aqui se guardan los pares que dieron una respuesta incorrecta para su análisis
    for i in range(count_tests):   #repetimos el ciclo count_tests veces
        x = randint(1, ran_x)    #creamos variables random de x e y, acotadas por ran_x y ran_y, es necesaria la cota porque 
        y = randint(1, ran_y) #al utilizar el algoritmo por fuerza bruta para valores grandes de las variables demorará en validar la respuesta
        if (CountSpecialsPairs_NT(x, y) == CountSpecialsPairs_BF(x, y)): #comprobamos si son iguales ambos resultados
            results.append("Correct") 
        else:                                      #guardamos los resultados en sus respectivas listas
            results.append("Incorrect")
            incorrects.append((x,y))
    print(results)
    print(incorrects)      #finalmente imprimimos los resultados alcanzados


    