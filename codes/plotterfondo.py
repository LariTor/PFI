import matplotlib.pyplot as plt
import sys

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        # Leer las líneas del archivo y filtrar las líneas vacías
        lineas = [linea.strip() for linea in archivo.readlines() if linea.strip()]
        # Convertir las líneas restantes a números flotantes
        vector = [float(linea) for linea in lineas]
    return vector

def single_plotter(nombre_fondo):
    fondo = leer_archivo(nombre_fondo)
    # Generar el vector de números de fila del archivo (asumiendo que ambos archivos tienen la misma longitud)
    numeros_de_fila = list(range(1, len(fondo) + 1))

    plt.semilogy(numeros_de_fila, fondo)
    plt.xlabel('Número de fila del archivo')
    plt.ylabel('Fondo')
    plt.title(nombre_fondo)
    #plt.savefig(nombre_archivo, bbox_inches='tight')    ##UNCOMMENT FOR SAVEIMAGES, NOT SHOW
    plt.clf()
    #plt.show()

def multi_plotter_fondos(nombre_fondo, ax):
    fondo = leer_archivo(nombre_fondo)
    # Generar el vector de números de fila del archivo (asumiendo que ambos archivos tienen la misma longitud)
    numeros_de_fila = list(range(1, len(fondo) + 1))
    #grafico
    ax.semilogy(numeros_de_fila, fondo, label=nombre_fondo)


for fondo in sys.argv[1:]:
    if not fondo.endswith('.png'):
        single_plotter(fondo)
plt.close()
fig, ax = plt.subplots()
for fondo in sys.argv[1:]:
    if not fondo.endswith('.png'):
        multi_plotter_fondos(fondo, ax)
plt.xlabel('Número de fila del archivo')
plt.ylabel('Diferencia con el fondo')
plt.title('Multiplot')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.savefig('Multiplot', bbox_inches='tight') ##UNCOMMENT FOR SAVEIMAGES, NOT SHOW
plt.show()