
import Classes
from Classes import *
from Classes import Gui

# Importacion de las librerias necesarias
if __name__ == '__main__':
    # Creamos la instancia principal de Root
    root = tk.Tk()

    # Le pasamo a Gui el control de la ventana
    ventana = Gui(root)

    # Se crea una instancia de la clase Gui y se llama al metodo recuperar variables de control
    # Esto crea una lista con los nombre de las variables que son seleccionadas


    # Bucle principal de la ventana
    root.mainloop()