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

def main(fondo, archivo):

    archivo1 = leer_archivo(archivo)

    fondo1 = leer_archivo(fondo)
    
    diferenciaVar = diferencia(archivo1,fondo1)

    # Generar el vector de números de fila del archivo (asumiendo que ambos archivos tienen la misma longitud)
    numeros_de_fila = list(range(1, len(diferenciaVar) + 1))


    # Graficar la diferencia entre archivo y fondo

   

    linea = plt.semilogy(numeros_de_fila, diferenciaVar, label='Diferencia Directo50AMP y AcopleDIRECTO')

    plt.xlabel('Número de fila del archivo')
    plt.ylabel('Diferencia')
    plt.title('50 AMPLIFICACIÓN')
    plt.legend(handles=[linea], loc='upper right', bbox_to_anchor=(1.25, 1))
   