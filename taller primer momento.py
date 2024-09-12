"""             TALLER PRIMER MOMENTO -- CRISTIAN CAMILO MOLINA DUQUE - SABADO 10.30

1)	Elabore un programa para la Universidad de Florida que
- calcule los primeros 100 números de la siguiente serie 5, 8, 13, 21, ...
-sin mostrar el 13, y muestre la lista del resultado de los números."""


def secuenciaFlorida():
    # Creamos la serie inicial
    serie = [5, 8, 13, 21]

    # Procesamos los datos como lo necesitamos
    while len(serie) < 100:
        siguiente_numero = serie[-1] + serie[-2]
        serie.append(siguiente_numero)

    # Excluir el número 13 al imprimir
    exclusion = 13
    for numero in serie:
        if numero != exclusion:
            print(numero)

    return serie

# Llamada a la función
secuenciaFlorida()

"""
2)	Elabore un programa para el Éxito que 
-determine el salario de los 1897 empleados de su compañía, 
-teniendo en cuenta las comisiones y la seguridad social que debe pagar, e 
-imprima el listado de la información. 
"""

# Definimos las variables
empleados = 5
constSalario = 1300000
constSeguridad = 64000

# Procesamos datos
for i in range(empleados):
    nombre = input("Ingresa el nombre del empleado: ")
    comision = int(input("Ingresa el valor de la comisión: "))

    # Cálculo de salario total
    total_pagar = constSalario + comision - constSeguridad

    # Imprimir resultados
    print(f"\nEmpleado: {nombre}")
    print(f"Comisión: {comision}")
    print(f"Descuentos: {constSeguridad}")
    print(f"Total a pagar: {total_pagar}\n")

"""
3)	Elabore un programa para la facultad de Ingeniería que 
pida 400 números e indique si ese número es par o impar; 
me muestre un listado 
y me indique cuantos son pares y cuantos son impares.
"""


# Definimos los Contadores
cantidad_pares = 0
cantidad_impares = 0

# Creamos el  ciclo
for i in range(1, 401):
    numero = int(input(f"Ingrese el número {i}: "))

    # Verificamos si el número es par o impar
    if numero % 2 == 0:
        print(f"El número {numero} es par")
        cantidad_pares += 1  # Aumentamos el contador de pares
    else:
        print(f"El número {numero} es impar")
        cantidad_impares += 1  # Aumentamos el contador de impares

# Mostramos cuántos números fueron pares e impares
print("\nResultados:")
print(f"Total de números pares: {cantidad_pares}")
print(f"Total de números impares: {cantidad_impares}")

"""
4) Elabore un programa para un Hospital que determine, 
y muestre el nivel de Leucemia de 803 pacientes 
clasificando su puntaje si esta inferior a 10 no tiene Leucemia;
 si esta entre 11 y 40, nivel bajo de Leucemia; 
 si esta entre 40 y 69, nivel moderado de Leucemia,
  si esta entre 70 y 100, nivel grave de Leucemia.
"""

# Contadores para los diferentes niveles de leucemia
sin_leucemia = 0
leucemia_baja = 0
leucemia_moderada = 0
leucemia_grave = 0

# Procesamos 803 pacientes
for i in range(1, 804):
    # Pedimos el puntaje de leucemia del paciente
    puntaje = int(input(f"Ingrese el puntaje del paciente {i}: "))

    # Clasificamos según el puntaje
    if puntaje < 10:
        print(f"Paciente {i}: No tiene Leucemia")
        sin_leucemia += 1
    elif 11 <= puntaje <= 40:
        print(f"Paciente {i}: Nivel bajo de Leucemia")
        leucemia_baja += 1
    elif 41 <= puntaje <= 69:
        print(f"Paciente {i}: Nivel moderado de Leucemia")
        leucemia_moderada += 1
    elif 70 <= puntaje <= 100:
        print(f"Paciente {i}: Nivel grave de Leucemia")
        leucemia_grave += 1
    else:
        print(f"Paciente {i}: Puntaje fuera de rango. Ingrese un valor entre 0 y 100.")

# Mostramos el resumen de resultados
print("\nResumen:")
print(f"Pacientes sin Leucemia: {sin_leucemia}")
print(f"Pacientes con nivel bajo de Leucemia: {leucemia_baja}")
print(f"Pacientes con nivel moderado de Leucemia: {leucemia_moderada}")
print(f"Pacientes con nivel grave de Leucemia: {leucemia_grave}")


"""
5)	Elabore un programa para determinar el funcionamiento optimo de las 407 cabinas de metro cable,
 registrando un puntaje que se clasifica de la siguiente forma
  si tiene 2 puntos está con un funcionamiento defectuoso,
   si tiene 3 puntos el funcionamiento es moderado
    y si tiene 4 puntos el funcionamiento es óptimo.
"""

# Contadores para los diferentes niveles de funcionamiento
defectuoso = 0
moderado = 0
optimo = 0

# Procesamos las 407 cabinas
for i in range(1, 408):
    # Pedimos el puntaje de funcionamiento de la cabina
    puntaje = int(input(f"Ingrese el puntaje de la cabina {i} (2, 3 o 4): "))

    # Clasificamos según el puntaje
    if puntaje == 2:
        print(f"Cabina {i}: Funcionamiento defectuoso")
        defectuoso += 1
    elif puntaje == 3:
        print(f"Cabina {i}: Funcionamiento moderado")
        moderado += 1
    elif puntaje == 4:
        print(f"Cabina {i}: Funcionamiento óptimo")
        optimo += 1
    else:
        print(f"Cabina {i}: Puntaje inválido. Debe ser 2, 3 o 4.")

# Mostramos el resumen de resultados
print("\nResumen de funcionamiento de las cabinas:")
print(f"Cabinas con funcionamiento defectuoso: {defectuoso}")
print(f"Cabinas con funcionamiento moderado: {moderado}")
print(f"Cabinas con funcionamiento óptimo: {optimo}")







