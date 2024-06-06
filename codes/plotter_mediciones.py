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

# Dividir las etiquetas en dos grupos
labels = list(lines_by_label.keys())
half_length = len(labels) // 2
left_labels = labels[:half_length]
right_labels = labels[half_length:]

# Crear checkbuttons para las etiquetas de la izquierda
line_colors_left = [lines_by_label[label].get_color() for label in left_labels]
rax_left = plt.axes([0.05, 0.0, 0.4, 0.2])
check_left = CheckButtons(
    ax=rax_left,
    labels=left_labels,
    actives=[True] * len(left_labels),
    label_props={'color': line_colors_left},
    #frame_props={'edgecolor': line_colors_left},
    check_props={'facecolor': line_colors_left},
)

# Función de devolución de llamada para checkbuttons de la izquierda
def callback_left(label):
    ln = lines_by_label[label]
    ln.set_visible(not ln.get_visible())
    plt.draw()

check_left.on_clicked(callback_left)

# Crear checkbuttons para las etiquetas de la derecha
line_colors_right = [lines_by_label[label].get_color() for label in right_labels]
rax_right = plt.axes([0.55, 0.0, 0.4, 0.2])
check_right = CheckButtons(
    ax=rax_right,
    labels=right_labels,
    actives=[True] * len(right_labels),
    label_props={'color': line_colors_right},
    #frame_props={'edgecolor': line_colors_right},
    check_props={'facecolor': line_colors_right},
)

# Función de devolución de llamada para checkbuttons de la derecha
def callback_right(label):
    ln = lines_by_label[label]
    ln.set_visible(not ln.get_visible())
    plt.draw()

check_right.on_clicked(callback_right)

# Ajustes de estilo de los checkbuttons
for check in (check_left, check_right):
    check.labelpad = 0.1  # Aumentar el espacio entre el cuadro de verificación y el texto de la etiqueta
    check.ax.tick_params(labelsize='small')  # Tamaño del texto de la etiqueta

plt.subplots_adjust(top=0.950,bottom=0.280,left=0.050, right=0.9)  # Ajuste de la posición del gráfico

plt.show()