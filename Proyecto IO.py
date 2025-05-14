
import random

print("Ingrese 0 para crear la matriz de forma manual\nIngrese 1 para crear la matriz de forma aleatoria");
elegir = int(input());
filas= int(input("\ningrese el numero de filas:  "))
columnas = int(input("\ningrese el numero de  columnas:  "))
matriz=[]
fila_actual=[]
combinacion = random.choice([random.randint, random.uniform])
probabilidad = (1/columnas)



acumulador_fila=0;
acumulador_columna=0;


# para generar matriz manual
if elegir == 0:
    
    for i in  range(filas):
        fila_actual=[];
        for j in range (columnas):
            valor = float(input((f"\nIngrese el valor para la fila{i}, columna{j}: ")));
            fila_actual.append(valor)
        matriz.append(fila_actual)
    for fila in matriz:
            print(f"\n{fila}")
    


# para generar matriz aleatoria

elif elegir == 1:

    for i in  range(filas):
        fila_actual=[];
        for j in range (columnas):
            valor = combinacion(1,100)
            fila_actual.append(valor)
        matriz.append(fila_actual)
    for fila in matriz:
        print(f"\n{fila}" )
    

#criterio de  Laplace

#valor_Laplace=0;

#for k in range(filas):
    #valor_Mayor = 0
    #for l in range(columnas):
        #valor_Mayor += matriz[k][l] * probabilidad
      
    #print(f"\nAlternativa {k+1} = {valor_Mayor}")

    #if suma >valor_Laplace:
        #valor_Laplace = suma
#print(f"\nEl valor esperado es:  {valor_Laplace}")



#criterio de  optimista


#valor_optimista = 0


#for n in range (columnas):
    #comparar_columnas = 0
    #for m in range(filas):
        #comparar_columnas= matriz[m][n]
        #if matriz[m][n]> comparar_columnas:
            #comparar_columnas = matriz[m][n]
    #print(f"\nAlternativa {n+1} = {comparar_columnas}")
            
    #if comparar_columnas>valor_optimista:
        #valor_optimista= comparar_columnas

       
#print(f"\nEl mejor valor es : {valor_optimista}")
       

#criterio pesimista

#valor_pesimista = -float("inf")

#for o in range (filas):
    #valor_minimo = matriz[o][0]
    
    #for p in range(1,columnas):
        #if matriz[o][p]<valor_minimo:
            #valor_minimo= matriz[o][p]
            
    #print(f"\nAlternativa {o+1} = {valor_minimo}")
            
#if valor_minimo>valor_pesimista:
    #valor_pesimista = valor_minimo

       
#print(f"\nSégun el criterio pesimista se debe elegir la alternativa: {valor_minimo}")
       


