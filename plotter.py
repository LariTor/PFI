import matplotlib.pyplot as plt

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        # Leer las líneas del archivo y filtrar las líneas vacías
        lineas = [linea.strip() for linea in archivo.readlines() if linea.strip()]
        # Convertir las líneas restantes a números flotantes
        vector = [float(linea) for linea in lineas]
    return vector

def diferencia(archivo1, archivo2):
    vector1 = leer_archivo(archivo1)
    vector2 = leer_archivo(archivo2)

    # Asegurarse de que ambos vectores tengan la misma longitud
    min_length = min(len(vector1), len(vector2))
    vector1 = vector1[:min_length]
    vector2 = vector2[:min_length]

    # Calcular la diferencia entre los dos vectores y devolverla
    return [v1 - v2 for v1, v2 in zip(vector1, vector2)]

# Luego puedes llamar a esta función en cualquier lugar del código según tus necesidades
diferencia_acople50_acoplefondo = diferencia('AcopleFibra50AMP.txt', 'AcopleFONDO.txt')
diferencia_directo50_directofondo = diferencia('Directo50AMP.txt', 'DirectoFONDO.txt')

diferencia_acople100_acoplefondo = diferencia('AcopleFibra100AMP.txt', 'AcopleFONDO.txt')
diferencia_directo100_directofondo = diferencia('Directo100AMP.txt', 'DirectoFONDO.txt')

diferencia_acople200_acoplefondo = diferencia('AcopleFibra200AMP.txt', 'AcopleFONDO.txt')
diferencia_directo200_directofondo = diferencia('Directo200AMP.txt', 'DirectoFONDO.txt')

diferencia_acople500_acoplefondo = diferencia('AcopleFibra500AMP.txt', 'AcopleFONDO.txt')
diferencia_directo500_directofondo = diferencia('Directo500AMP.txt', 'DirectoFONDO.txt') 

# Generar el vector de números de fila del archivo (asumiendo que ambos archivos tienen la misma longitud)
numeros_de_fila = list(range(1, min(len(diferencia_acople50_acoplefondo), len(diferencia_directo50_directofondo)) + 1))


# Graficar la diferencia entre AcopleFibra50AMP y AcopleFONDO
plt.figure(figsize=(10, 5))
linea1, = plt.semilogy(numeros_de_fila, diferencia_acople50_acoplefondo, label='Diferencia AcopleFibra50AMP y AcopleFONDO')

# Graficar la diferencia entre Directo50AMP y AcopleDIRECTO
linea2, = plt.semilogy(numeros_de_fila, diferencia_directo50_directofondo, label='Diferencia Directo50AMP y AcopleDIRECTO')

plt.xlabel('Número de fila del archivo')
plt.ylabel('Diferencia')
plt.title('50 AMPLIFICACIÓN')
plt.legend(handles=[linea1, linea2], loc='upper right', bbox_to_anchor=(1.25, 1))
linea1.set_visible(True)  # Define si el plot correspondiente a la primera leyenda está visible
linea2.set_visible(True)  # Define si el plot correspondiente a la segunda leyenda está visible
###############################
# Graficar la diferencia entre AcopleFibra100AMP y AcopleFONDO
plt.figure(figsize=(10, 5))
linea3, = plt.semilogy(numeros_de_fila, diferencia_acople100_acoplefondo, label='Diferencia AcopleFibra100AMP y AcopleFONDO')

# Graficar la diferencia entre Directo100AMP y AcopleDIRECTO
linea4, = plt.semilogy(numeros_de_fila, diferencia_directo100_directofondo, label='Diferencia Directo100AMP y AcopleDIRECTO')

plt.xlabel('Número de fila del archivo')
plt.ylabel('Diferencia')
plt.title('100 AMPLIFICACIÓN')
plt.legend(handles=[linea3, linea4], loc='upper right', bbox_to_anchor=(1.25, 1))
linea3.set_visible(False)  # Define si el plot correspondiente a la primera leyenda está visible
linea4.set_visible(False)  # Define si el plot correspondiente a la segunda leyenda está visible
##########################3
# Graficar la diferencia entre AcopleFibra200AMP y AcopleFONDO
plt.figure(figsize=(10, 5))
linea5, = plt.semilogy(numeros_de_fila, diferencia_acople200_acoplefondo, label='Diferencia AcopleFibra200AMP y AcopleFONDO')

# Graficar la diferencia entre Directo200AMP y AcopleDIRECTO
linea6, = plt.semilogy(numeros_de_fila, diferencia_directo200_directofondo, label='Diferencia Directo200AMP y AcopleDIRECTO')

plt.xlabel('Número de fila del archivo')
plt.ylabel('Diferencia')
plt.title('200 AMPLIFICACIÓN')
plt.legend(handles=[linea5, linea6], loc='upper right', bbox_to_anchor=(1.25, 1))
linea5.set_visible(True)  # Define si el plot correspondiente a la primera leyenda está visible
linea6.set_visible(True)  # Define si el plot correspondiente a la segunda leyenda está visible
acoplefibra200 = leer_archivo("AcopleFibra200AMP.txt")
fondofibra = leer_archivo("AcopleFONDO.txt")
plt.figure(figsize=(10,5))
plt.semilogy(numeros_de_fila, acoplefibra200, label = 'Fibra')
plt.semilogy(numeros_de_fila, fondofibra, label = 'Fondo')
plt.xlabel('Número de fila del archivo')
plt.ylabel('Cuentas')
plt.title('200 AMPLIFICACIÓN - ACOPLE FIBRA VS FONDO')


directo200 = leer_archivo("Directo200AMP.txt")
fondodirecto = leer_archivo("DirectoFONDO.txt")
plt.figure(figsize=(10,5))
plt.semilogy(numeros_de_fila, directo200, label='Directo')
plt.semilogy(numeros_de_fila, fondodirecto, label = 'Fondo')
plt.xlabel('Número de fila del archivo')
plt.ylabel('Cuentas')
plt.title('200 AMPLIFICACIÓN - DIRECTO VS FONDO')

##############################
# Graficar la diferencia entre AcopleFibra500AMP y AcopleFONDO
plt.figure(figsize=(10, 5))
linea7, = plt.semilogy(numeros_de_fila, diferencia_acople500_acoplefondo, label='Diferencia AcopleFibra500AMP y AcopleFONDO')

# Graficar la diferencia entre Directo500AMP y AcopleDIRECTO
linea8, = plt.semilogy(numeros_de_fila, diferencia_directo500_directofondo, label='Diferencia Directo500AMP y AcopleDIRECTO')

plt.xlabel('Número de fila del archivo')
plt.ylabel('Diferencia')
plt.title('500 AMPLIFICACIÓN')

plt.legend(handles=[linea7, linea8], loc='upper right', bbox_to_anchor=(1.25, 1))
linea3.set_visible(True)  # Define si el plot correspondiente a la primera leyenda está visible
linea4.set_visible(True)  # Define si el plot correspondiente a la segunda leyenda está visible

acoplefibra500 = leer_archivo("AcopleFibra500AMP.txt")
fondofibra = leer_archivo("AcopleFONDO.txt")
plt.figure(figsize=(10,5))
plt.semilogy(numeros_de_fila, acoplefibra500, label = 'Fibra')
plt.semilogy(numeros_de_fila, fondofibra, label = 'Fondo')
plt.xlabel('Número de fila del archivo')
plt.ylabel('Cuentas')
plt.title('500 AMPLIFICACIÓN - ACOPLE FIBRA VS FONDO')


directo500 = leer_archivo("Directo500AMP.txt")
fondodirecto = leer_archivo("DirectoFONDO.txt")
plt.figure(figsize=(10,5))
plt.semilogy(numeros_de_fila, directo500, label='Directo')
plt.semilogy(numeros_de_fila, fondodirecto, label = 'Fondo')
plt.xlabel('Número de fila del archivo')
plt.ylabel('Cuentas')
plt.title('500 AMPLIFICACIÓN - DIRECTO VS FONDO')
plt.show()