import matplotlib.pyplot as plt
import sys

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        # Leer las líneas del archivo y filtrar las líneas vacías
        lineas = [linea.strip() for linea in archivo.readlines() if linea.strip()]
        # Convertir las líneas restantes a números flotantes
        vector = [float(linea) for linea in lineas]
    return vector

def diferencia(vector1, vector2):
    # Asegurarse de que ambos vectores tengan la misma longitud
    min_length = min(len(vector1), len(vector2))
    vector1 = vector1[:min_length]
    vector2 = vector2[:min_length]

    # Calcular la diferencia entre los dos vectores y devolverla
    return [v1 - v2 for v1, v2 in zip(vector1, vector2)]

def single_plotter(nombre_fondo, nombre_archivo):
    archivo = leer_archivo(nombre_archivo)
    fondo = leer_archivo(nombre_fondo)
    diferenciaVar = diferencia(archivo,fondo)
    # Generar el vector de números de fila del archivo (asumiendo que ambos archivos tienen la misma longitud)
    numeros_de_fila = list(range(1, len(diferenciaVar) + 1))
    #grafico
    plt.semilogy(numeros_de_fila, diferenciaVar)
    plt.xlabel('Número de fila del archivo')
    plt.ylabel('Diferencia con el fondo')
    plt.title(nombre_archivo)
    #plt.savefig(nombre_archivo, bbox_inches='tight')    ##UNCOMMENT FOR SAVEIMAGES, NOT SHOW
    #plt.clf()
    plt.show()

def multi_plotter(nombre_fondo, nombre_archivo, ax):
    archivo = leer_archivo(nombre_archivo)
    fondo = leer_archivo(nombre_fondo)
    diferenciaVar = diferencia(archivo,fondo)
    # Generar el vector de números de fila del archivo (asumiendo que ambos archivos tienen la misma longitud)
    numeros_de_fila = list(range(1, len(diferenciaVar) + 1))
    #grafico
    ax.semilogy(numeros_de_fila, diferenciaVar, label=nombre_archivo)

# plotter.py    fondo          *
# argv[0]      argv[1]    argv[2....n]
fondo = sys.argv[1]

for archivo in sys.argv[2:]:
    if archivo != fondo and not archivo.endswith('.png'):
        single_plotter(fondo,archivo)
plt.close()
fig, ax = plt.subplots()
for archivo in sys.argv[2:]:
    if archivo != fondo and not archivo.endswith('.png'):
        multi_plotter(fondo,archivo, ax)
plt.xlabel('Número de fila del archivo')
plt.ylabel('Diferencia con el fondo')
plt.title('Multiplot')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.savefig('Multiplot', bbox_inches='tight') ##UNCOMMENT FOR SAVEIMAGES, NOT SHOW
plt.show()