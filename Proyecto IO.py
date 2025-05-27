



import random


def menu():
    
    print("\nIngrese una de las siguientes opciones: "
          "\n1. Criterio de Laplace."
          "\n2. Criterio Optimista."
          "\n3. Criterio Pesimista."
          "\n4. Criterio de Hurwicz."
          "\n5. Criterio de Savage."
          "\n6. Salir")    


def seleccion():
    while True:
        try:    
            elegir = int(input("Ingrese 0 para crear la matriz de forma manual\nIngrese 1 para crear la matriz de forma aleatoria: \n"));

            if elegir  not in [0,1]:
                print("¡Error! ingrese  0 o 1.")
                continue
            
            filas= int(input("\ningrese el numero de filas:  \n"))
            columnas = int(input("\ningrese el numero de  columnas:  \n"))
            matriz=[]
            fila_actual=[]
            combinacion = random.choice([random.randint, random.uniform])
            probabilidad = (1/columnas)
            
    

    # para generar matriz manual
            if elegir == 0:
    
                for i in  range(filas):
                    fila_actual=[];
                    for j in range (columnas):
                        valor = float(input((f"\nIngrese el valor para la fila{i}, columna{j}: ")));
                        fila_actual.append(valor)
                    matriz.append(fila_actual)
                for fila in matriz:
                    print(f"\n{fila}\n")

                return matriz,filas,columnas,probabilidad
        
        

# para generar matriz aleatoria

            elif elegir == 1:

                for i in  range(filas):
                    fila_actual=[];
                    for j in range (columnas):
                        valor = combinacion(-5000,5000)
                        fila_actual.append(valor)
                    matriz.append(fila_actual)
                for fila in matriz:
                    print(f"\n{fila}\n")
        
                return matriz,filas,columnas,probabilidad

        except ValueError:
            print("¡Entrada inválida! Ingrese una opción valida (0 o 1).")

        
              
while True:
    menu()
    
    try:

        opcion = int(input())
        

#criterio de Laplace

        

        if opcion == 1:
            print("Usted ha elegido el criterio de Laplace\n")

            matriz,filas,columnas,probabilidad =seleccion()

            valor_Laplace=0;
            
            for k in range(filas):
                valor_mayor = 0
                for l in range(columnas):
                    valor_mayor += matriz[k][l] * probabilidad
      
                print(f"\nAlternativa {k+1} = {valor_mayor}")

                if valor_mayor >valor_Laplace:
                    valor_Laplace = valor_mayor
            print(f"\nEl valor esperado, según el criterio de Laplace es:{valor_Laplace}")
            
        
#Citerio Optimista
                 
        elif opcion == 2:
            print("\nUsted ha elegido el criterio de Optimista\n")

            matriz,filas,columnas,valor_optimista = seleccion()

            valor_optimista = 0
            for m in range (filas):
                comparar_fila = matriz[m][0]
                for n in range(1,columnas):
                    if matriz[m][n]> comparar_fila:
                        comparar_fila = matriz[m][n]
                print(f"\nAlternativa {m+1} = {comparar_fila}")
            
                if comparar_fila>valor_optimista:
                    valor_optimista= comparar_fila

       
            print(f"\nEl valor esperado, según el criterio optimista es:{valor_optimista}")
            
       
#Citerio Pesimista
            
                 
        elif opcion == 3:
            print("\nUsted ha elegido el criterio pesimista\n")

            matriz,filas,columnas,valor_pesimista= seleccion()

            valor_pesimista = -float("inf")
        
            for o in range (filas):
                valor_minimo = matriz[o][0]
                for p in range(1,columnas):
                    if matriz[o][p]<valor_minimo:
                        valor_minimo= matriz[o][p]
            
                print(f"\nAlternativa {o+1} = {valor_minimo}") 
            
                if valor_minimo>valor_pesimista:
                    valor_pesimista = valor_minimo

       
            print(f"\nEl valor esperado, según el criterio pesismista es :{valor_pesimista}")



#Criterio de Hurwicz
                
        elif opcion == 4:
            print("\nUsted ha elegido el criterio de Hurwicz\n")
            matriz,filas,columnas,valor_maximo_hurwicz = seleccion()


            while True:

                try:

                    coeficiente = float(input("Ingrese el coeficiente de optimismo comprendido entre 0 a 1: "))
                    coeficiente_valores_minimos = (1-(coeficiente))

                    if 0 <= coeficiente <=1:
                        coeficiente
                        break
                    else:
                        print("\n¡Valor incorrecto!. Ingrese un valor entre 0 y 1")

                
                except ValueError:
                        print("\n¡Valor invalido!. Ingrese un valor entre 0 y 1")


            valor_minimo= float("inf")
            valor_maximo=-float("inf")
            matriz_hurwicz=[]
            resultado_min=0
            resultado_max=0
            resultado_final=0
            valor_maximo_hurwicz=0


            for q in range(filas):
                valor_mayor_fila = matriz[q][0]
                valor_menor_fila= matriz[q][0]

                for r in range (1,columnas):
                    if matriz[q][r]> valor_mayor_fila:
                        valor_mayor_fila=matriz[q][r]

                    if matriz[q][r]< valor_menor_fila:
                        valor_menor_fila=matriz[q][r]
       
                resultado_max = valor_mayor_fila*coeficiente                                
                resultado_min = valor_menor_fila* coeficiente_valores_minimos
                resultado_final= resultado_max +resultado_min

                matriz_hurwicz.append(resultado_final)
                print(f"\nAlternativa {q+1} = {resultado_final}")
                valor_maximo_hurwicz = max(matriz_hurwicz)
      
            print(f"\nEl valor esperado, según el criterio de Hurwicz  es :{valor_maximo_hurwicz}")




 #criterio de savage
            

        elif opcion == 5:
            print("\nUsted ha elegido el criterio de Savage\n")

            matriz,filas,columnas,matriz_savage = seleccion()


            resta_filas=0
            valores_filas=[]
            valor_max_columna=[]
            matriz_savage=[]

            valor_savage=0

            for t in range(columnas):
                valor_maximo = matriz[0][t]
                for s in range(filas):
                    if matriz[s][t] > valor_maximo:
                        valor_maximo = matriz[s][t]
                valor_max_columna.append(valor_maximo)
                        
            for s in range(filas):
                nueva_matriz=[]
                for t in range (columnas):
                    resta_filas= valor_max_columna[t] - matriz[s][t]
                    nueva_matriz.append(resta_filas)
                matriz_savage.append(nueva_matriz)

            print(f"\nMatriz de Beneficios Esperados\n")
            for fila in matriz_savage:
                print(f"\n{fila}\n")


            valores_filas.sort()
            for i in range(len(matriz_savage)):
                numero_mayor= matriz_savage[i]
                valor_maximo_fila = max(numero_mayor)
                valores_filas.append(valor_maximo_fila)
                print(f"\nAlternativa {i+1} = {valor_maximo_fila} ")

            valores_filas.sort()
            valor_central = min(valores_filas)
            print(f"\nEl valor Esperado, según el criterio de Savage es:{valor_central}")


        elif opcion == 6:
            print("\n¡Hasta pronto\n")
            break
        else:
            print("\n¡Opción inválida! Por favor, ingrese una opción válida (1 a 6).\n")
            menu()

    except ValueError:
            print("\n¡Entrada inválida! Por favor, ingrese una opción válida (1 a 6)\n")
