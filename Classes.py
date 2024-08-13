from tkinter import font,messagebox,PhotoImage
import tkinter as tk
import subprocess


class Gui:
    """
    La clase Gui es la encargada de crear toda la interfaz
    de usuario los botones frames y labels en su constructor.

    Metodos:
    -__init__(self, root)
    -recuperador_variales_de_control(self) -> List[]
    -iniciar_instalacion(self)
    """
    def __init__(self, root):
        """
        Cosntrucctor de la clase Gui

        ARS:
        -root: Es la instancia de la ventana principal de Tk()
        """
        #=========================  Constantes =========================
        # colores
        celeste_claro = "#00BCD4"
        gris = "#D9D9D9"


        # Fuente
        fuente_lemon = font.Font(family="Lemon", size=8)

        # ========================= Ventana principal =========================
        self.ventana = root
        self.ventana.title("Developer Kit")  # Titulo
        self.ventana.config(width=450, height=305,bg=celeste_claro)  # Dimensiones de la ventana principal
        self.ventana.resizable(0, 0)  # Redimensionable OFF
        self.ventana.iconbitmap("recursos/icons/icon.ico")  # Icono de la ventana

        #========================= Label "Developer Kit" =========================
        self.titulo_Programa = tk.Label(master=self.ventana,
                                        bg=celeste_claro,
                                        text="Developer Kit\nBy VesuDev",
                                        font=fuente_lemon)
        self.titulo_Programa.config(width=12, height=2)
        self.titulo_Programa.place(x=0, y=255)

        #========================= Label "Seleccione los Programas" =========================
        flecha_abajo = "\u2193"
        self.titulo_Scroll_Bar = tk.Label(self.ventana,
                                          font=fuente_lemon,
                                          bg=celeste_claro,
                                          text=f"{flecha_abajo}Seleccione los programas que desea instalar{flecha_abajo}")
        self.titulo_Scroll_Bar.config(width=40, height=1)
        self.titulo_Scroll_Bar.place(x=45, y=25)


        #========================= Frame principal de la ventana =========================
        self.frame_principal = tk.Frame(self.ventana,bg=gris, width=430, height=215, relief="solid", borderwidth=2)
        self.frame_principal.place(x=10, y=45)

        # ======================== Logos de programas ==========================
        # --------------------------- Logo Vscode ----------------------------
        self.logo_vscode = PhotoImage(file="recursos/image/vscode.png")
        self.label_Vscode = tk.Label(self.frame_principal, image=self.logo_vscode,bg=gris)
        self.label_Vscode.place(x=0,y=0)

        # --------------------------- Logo Android Studio ----------------------------
        self.logo_android_studio = PhotoImage(file="recursos/image/android_studio.png")
        self.label_android_studio = tk.Label(self.frame_principal, image=self.logo_android_studio,bg=gris)
        self.label_android_studio.place(x=0, y=40)

        # --------------------------- Subime text ----------------------------
        self.logo_sublime_text = PhotoImage(file="recursos/image/sublimeText.png")
        self.label_sublime_text = tk.Label(self.frame_principal, image=self.logo_sublime_text, bg=gris)
        self.label_sublime_text.place(x=0, y=82)

        # --------------------------- Git ----------------------------
        self.logo_git = PhotoImage(file="recursos/image/git.png")
        self.label_git = tk.Label(self.frame_principal, image=self.logo_git,bg=gris)
        self.label_git.place(x=0,y=125)

        # --------------------------- intellij ----------------------------
        self.logo_intellij = PhotoImage(file="recursos/image/intellij.png")
        self.label_intellij = tk.Label(self.frame_principal, image=self.logo_intellij,bg=gris)
        self.label_intellij.place(x=0, y=160)

        # --------------------------- PyCharm ----------------------------
        self.logo_pycharm = PhotoImage(file="recursos/image/pycharm.png")
        self.label_pycharm = tk.Label(self.frame_principal, image=self.logo_pycharm,bg=gris)
        self.label_pycharm.place(x=190, y=2)

        # --------------------------- Pc_Automatizacion Image ----------------------------
        self.logo_pc = PhotoImage(file="recursos/image/pc_automatization.png")
        self.label_pc = tk.Label(self.frame_principal, image=self.logo_pc,bg=gris)
        self.label_pc.place(x=205, y=40)

        # ============================= Check boxes =========================
        # ---------------------- Visual Studio Code ---------------------
        self.vs_code_var = tk.BooleanVar()
        self.vs_code_CheckButton = tk.Checkbutton(self.frame_principal,
                                       onvalue=True,
                                       offvalue=False,
                                       variable=self.vs_code_var,
                                       text="Visual Studio Code",bg=gris)
        self.vs_code_CheckButton.place(x=40,y=8)

        # -------------- Android Studio -----------------
        self.android_Studio_var = tk.BooleanVar()
        self.android_Studio_CheckButton = tk.Checkbutton(self.frame_principal,
                                          onvalue=True,
                                          offvalue=False,
                                          variable=self.android_Studio_var,
                                          text="Android Studio",bg=gris)
        self.android_Studio_CheckButton.place(x=40,y=50)

        # --------------------- Sublime Text -----------------
        self.sublime_text_var = tk.BooleanVar()
        self.sublime_text_CheckButton = tk.Checkbutton(self.frame_principal,
                                                       onvalue=True,
                                                       offvalue=False,
                                                       variable=self.sublime_text_var,
                                                       text="Sublime Text", bg=gris)
        self.sublime_text_CheckButton.place(x=40, y=90)

        # --------------------- Git -----------------
        self.git_var = tk.BooleanVar()
        self.git_CheckButton = tk.Checkbutton(self.frame_principal,
                                                     onvalue=True,
                                                     offvalue=False,
                                                     variable=self.git_var,
                                                     text="Git",bg=gris)
        self.git_CheckButton.place(x=40,y=130)

        # --------------------- IntelliJ -----------------
        self.intelliJ_var = tk.BooleanVar()
        self.intelliJ_CheckButton = tk.Checkbutton(self.frame_principal,
                                                     onvalue=True,
                                                     offvalue=False,
                                                     variable=self.intelliJ_var,
                                                     text="IntelliJ Community Edition",bg=gris)
        self.intelliJ_CheckButton.place(x=40,y=165)

        # --------------------- PyCharm -----------------
        self.pycharm_var = tk.BooleanVar()
        self.pycharm_CheckButton = tk.Checkbutton(self.frame_principal,
                                                     onvalue=True,
                                                     offvalue=False,
                                                     variable=self.pycharm_var,
                                                     text="PyCharm Community Edition",bg=gris)
        self.pycharm_CheckButton.place(x=222,y=8)


        # ==================== Botones ==============================

        # Instalar
        self.install_Button = tk.Button(self.ventana, text="Instalar",command=self.iniciar_instalacion,bg=gris)
        self.install_Button.config(width=8,bg=gris, height=1)
        self.install_Button.place(x=372, y=262)


    def recuperador_variales_de_control(self):
        """
        Este metodo retorna una lista el valor de las variables de control de los CheckBottom,
        y agrega a una lista el nombre de los programas cuya variable de control este en True.
        """
        lista_programas_selecciondos = []

        # si la variale es True significa que esta seleccionado
        if self.vs_code_var.get() == True:
            # se agrega a la lista de programas seleccinados
            lista_programas_selecciondos.append("Visual Studio code")

        if self.android_Studio_var.get() == True:
            lista_programas_selecciondos.append("Android Studio")

        if self.sublime_text_var.get() == True:
            lista_programas_selecciondos.append("Sublime Text")

        if self.git_var.get() == True:
            lista_programas_selecciondos.append("Git")

        if self.pycharm_var.get() == True:
            lista_programas_selecciondos.append("Py Charm Community Edition")

        if self.intelliJ_var.get() == True:
            lista_programas_selecciondos.append("IntelliJ Community Edition")

        # Esta funcion Regresa un Diccionario con los programas que furon seleccinados
        return lista_programas_selecciondos

    def iniciar_instalacion(self):
        """
        El metodo iniciar_instalacion toma la lista retornada por
        el metodo recuperador_variales_de_control() crea una
        instalncia de la clase Instalador() luego llama al
        metodo instalar() de la clase Instalador() y
        le pasa la lista de porgramas que se van a instalar.
        """
        lista_programas_seleccionados = self.recuperador_variales_de_control()

        instalador = Instalador()  # Crear una instancia de Instalador

        #se le pasa a instalador la lista de programas
        instalador.instalar(lista_programas_seleccionados)


class Instalador():
    """
    Esta Clase es la encargada de instalar con
    sus metodos los cada programa.

    Metodos:
    -Vscode_installer(self)
    -android_studio_installer(self)
    -sublime_text_installer(self)
    -git_installer(self)
    -pycharm_installer(self)
    -intellij_installer(self)
    -instalar(self,lista_programas_selecciondos).
    """
    def vscode_installer(self):
        """
        El Metodo ejecuta un subprocees.run() y accede a la ruta 'recursos/data/VScode.exe'.
        """

        print("iniciando instalacion de Visual studio code... ")
        try:
            # Guardamos la ruta del archivo en una variable
            vscode_path = "recursos/data/VScode.exe"
            # Ejecutamos el archivo con subprocess.run(path,command)
            resultado = subprocess.run([vscode_path,"/silent"])# NOTA: ese /silent hizo que mi programa se volviera 3 veces mas chico XD ya tenia los macros de mover el mouse jaja

            if resultado.returncode == 0:
                tk.messagebox.showinfo("Info","Instalacion completada correctamente")

            else:
                tk.messagebox.showerror("Error", "Error en la instalación de Visual Studio Code")


        except Exception as e:
            tk.messagebox.showwarning("Alerta!",f"A ocurrido un Error desconocido Error: {e}")

    def android_studio_installer(self):
        """
         El Metodo ejecuta un subprocees.run() y accede a la ruta 'recursos/data/Android-Studio.exe'.
        """
        print("iniciando instalacion de Android Studio... ")
        try:
            # Guardamos la ruta del archivo en una variable
            android_studio_path = "recursos/data/Android-Studio.exe"
            # Ejecutamos el archivo con subprocess.run
            resultado = subprocess.run([android_studio_path, "./studio.exe /S"])

            if resultado.returncode == 0:
                tk.messagebox.showinfo("Info", "Instalacion completada correctamente")


        except Exception as e:
            tk.messagebox.showwarning("Alerta!", f"A ocurrido un Error desconocido Error: {e}")

    def sublime_text_installer(self):
        """
        El Metodo ejecuta un subprocees.run() y accede a la ruta 'recursos/data/sublime text.exe'.
        """
        print("iniciando instalacion de Sublime Text... ")
        try:
            # Guardamos la ruta del archivo en una variable
            sublime_text_path = "recursos/data/sublime text.exe"
            # Ejecutamos el archivo con subprocess.run(path,command)
            resultado = subprocess.run([sublime_text_path])

            if resultado.returncode == 0:
                tk.messagebox.showinfo("Info", "Instalacion completada correctamente")
            else:
                tk.messagebox.showerror("Error", "Error en la instalación de Sublime Text")

        except Exception as e:
            tk.messagebox.showwarning("Alerta!", f"A ocurrido un Error desconocido Error: {e}")
    def git_installer(self):
        """
        El Metodo ejecuta un subprocees.run() y accede a la ruta 'recursos/data/Git.exe'.
        """

        print("iniciando instalacion de Sistema de Control de Versiones Git... ")
        try:
            # Guardamos la ruta del archivo en una variable
            git_path = "recursos/data/Git.exe"
            # Ejecutamos el archivo con subprocess.run(path,command)
            resultado = subprocess.run([git_path])

            if resultado.returncode == 0:
                tk.messagebox.showinfo("Info", "Instalacion completada correctamente")
            else:
                tk.messagebox.showerror("Error", "Error en la instalación del Sistema de Control de Versiones Git")

        except Exception as e:
            tk.messagebox.showwarning("Alerta!", f"A ocurrido un Error desconocido Error: {e}")
    def pycharm_installer(self):
        """
        El Metodo ejecuta un subprocees.run() y accede a la ruta 'recursos/data/PyCharm.exe'.
        """
        print("iniciando instalacion de PyCharm Community Edition... ")
        try:
            # Guardamos la ruta del archivo en una variable
            pycharm_path = "recursos/data/PyCharm.exe"
            # Ejecutamos el archivo con subprocess.run(path,command)
            resultado = subprocess.run([pycharm_path ,"/Silent"])

            if resultado.returncode == 0:
                tk.messagebox.showinfo("Info", "Instalacion completada correctamente")
            else:
                tk.messagebox.showerror("Error", "Error en la instalación de PyCharm Community Edition")

        except Exception as e:
            tk.messagebox.showwarning("Alerta!", f"A ocurrido un Error desconocido Error: {e}")
    def intellij_installer(self):
        """
        El Metodo ejecuta un subprocees.run() y accede a la ruta 'recursos/data/IntelliJ.exe'.
        """
        print("iniciando instalacion de IntelliJ Community Edition... ")
        try:
            # Guardamos la ruta del archivo en una variable
            intellij_path = "recursos/data/IntelliJ.exe"
            # Ejecutamos el archivo con subprocess.run(path,command)
            resultado = subprocess.run([intellij_path, "/Silent"])

            if resultado.returncode == 0:
                tk.messagebox.showinfo("Info", "Instalacion completada correctamente")
            else:
                tk.messagebox.showerror("Error", "Error en la instalación de IntelliJ Community Edition")

        except Exception as e:
            tk.messagebox.showwarning("Alerta!", f"A ocurrido un Error desconocido Error: {e}")

    def instalar(self,lista_programas_selecciondos):
        """
        Este metodo itera sobre la lista_recibida y
        verifica si el nombre en la lista es igual
        a el nombre de los programas si es asi llama
        a su funcion self.'programa'.intaller().
        """
        # Se itera la programa en lista de programas
        for programa in lista_programas_selecciondos:
            # Se llama al metodo correspondiente para cada
            if programa == "Visual Studio code":
                self.vscode_installer()

            elif programa == "Android Studio":
                self.android_studio_installer()

            elif programa == "Sublime Text":
                self.sublime_text_installer()

            elif programa == "Git":
                self.git_installer()

            elif programa == "Py Charm Community Edition":
                self.pycharm_installer()

            elif programa == "IntelliJ Community Edition":
                self.intellij_installer()

