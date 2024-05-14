import matplotlib.pyplot as plt
import sys
from matplotlib.widgets import CheckButtons

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = [linea.strip() for linea in archivo.readlines() if linea.strip()]
        vector = [float(linea) for linea in lineas]
    return vector

def multi_plotter_archivos(nombre_archivo, ax):
    archivo = leer_archivo(nombre_archivo)
    numeros_de_fila = list(range(1, len(archivo) + 1))
    ax.semilogy(numeros_de_fila, archivo, label=nombre_archivo)

# Diccionario para almacenar las líneas trazadas por etiqueta
lines_by_label = {}

fig, ax = plt.subplots()

for medicion in sys.argv[1:]:
    if not medicion.endswith('.png'):
        archivo = leer_archivo(medicion)
        numeros_de_fila = list(range(1, len(archivo) + 1))
        line, = ax.semilogy(numeros_de_fila, archivo, label=medicion)
        lines_by_label[medicion] = line

plt.xlabel('Número de fila del archivo')
plt.ylabel('Medicion')
plt.title('Multiplot')
#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Crear checkbuttons
line_colors = [l.get_color() for l in lines_by_label.values()]
rax = plt.axes([0.05, 0.0, 0.85, 0.2])
check = CheckButtons(
    ax=rax,
    labels=lines_by_label.keys(),
    actives=[True] * len(lines_by_label),
    label_props={'color': line_colors},
    #frame_props={'edgecolor': line_colors},
    check_props={'facecolor': line_colors},
)

# Función de devolución de llamada para checkbuttons
def callback(label):
    ln=lines_by_label[label]
    ln.set_visible(not ln.get_visible())
    plt.draw()
 #Ajustes de estilo de los checkbuttons
check.labelpad = 0.1  # Aumentar el espacio entre el cuadro de verificación y el texto de la etiqueta
check.ax.tick_params(labelsize='small')  # Tamaño del texto de la etiqueta

check.on_clicked(callback)
plt.subplots_adjust(top=0.950,bottom=0.240,left=0.050, right=0.9)  # Ajuste de la posición del gráfico

plt.show()