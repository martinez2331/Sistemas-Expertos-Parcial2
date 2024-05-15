import json

import tkinter as tk
from PIL import Image, ImageTk

from tkinter import simpledialog, messagebox



class MiVentana:
    def __init__(self, master, VenIm):
        self.VenIm = VenIm
        self.master = master
        self.personajes = self.cargar_personajes()
        self.respuestas = []
        self.personaje_adivinado = None
        self.contador = 0

        # Botones Sí y No
        self.boton_si = tk.Button(self.master, text="Sí", command=lambda: self.registrar_respuesta(True))
        self.boton_si.pack(side=tk.LEFT, padx=10)

        self.boton_no = tk.Button(self.master, text="No", command=lambda: self.registrar_respuesta(False))
        self.boton_no.pack(side=tk.LEFT, padx=10)

        # Etiqueta de pregunta
        self.lbl_preg = tk.Label(self.master, text="Selecciona una característica:")
        self.lbl_preg.pack()

        self.caracteristicas = list(self.personajes["finn"].keys())
        self.caracteristica_actual = self.caracteristicas[0]

        self.actualizar_pregunta()

    def cargar_personajes(self):
        try:
            with open("personajes.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {
                "finn": {
                    "tiene_gorra_blanca": "True",   
                    "tiene_mochila": "True",
                    "es_hombre": "True",
                    "tiene_cabello_rubio": "True",
                    "se_puede_estirar": "False",
                    "tiene_cabello_rosa": "False",
                    "tiene_vestido_rosa": "False",
                    "tiene_cabello_negro": "False",
                    "tiene_un_achagitarra": "False",
                    "tiene_botas_rojas": "False",
                    "tiene_cabello_pelirojo": "False",
                    "tiene_piel_azul": "False",
                    "tiene_un_guante_metalico": "False",
                    "tiene_corona": "False",
                    "tiene_cabello_blanco": "False",
                },
                "jake": {
                    "tiene_gorra_blanca": "False",   
                    "tiene_mochila": "False",
                    "es_hombre": "True",
                    "tiene_cabello_rubio": "True",
                    "se_puede_estirar": "True",
                    "tiene_cabello_rosa": "False",
                    "tiene_vestido_rosa": "False",
                    "tiene_cabello_negro": "False",
                    "tiene_un_achagitarra": "False",
                    "tiene_botas_rojas": "False",
                    "tiene_cabello_pelirojo": "False",
                    "tiene_piel_azul": "False",
                    "tiene_un_guante_metalico": "False",
                    "tiene_corona": "False",
                    "tiene_cabello_blanco": "False",
                },                
                "dulce_Princesa": {
                    "tiene_gorra_blanca": "False",   
                    "tiene_mochila": "False",
                    "es_hombre": "False",
                    "tiene_cabello_rubio": "False",
                    "se_puede_estirar": "False",
                    "tiene_cabello_rosa": "True",
                    "tiene_vestido_rosa": "True",
                    "tiene_cabello_negro": "False",
                    "tiene_un_achagitarra": "False",
                    "tiene_botas_rojas": "False",
                    "tiene_cabello_pelirojo": "False",
                    "tiene_piel_azul": "False",
                    "tiene_un_guante_metalico": "False",
                    "tiene_corona": "True",
                    "tiene_cabello_blanco": "False",
                },
                "marcelin": {
                    "tiene_gorra_blanca": "False",   
                    "tiene_mochila": "False",
                    "es_hombre": "False",
                    "tiene_cabello_rubio": "False",
                    "se_puede_estirar": "False",
                    "tiene_cabello_rosa": "False",                   
                    "tiene_vestido_rosa": "False",
                    "tiene_cabello_negro": "True",
                    "tiene_un_achagitarra": "True",
                    "tiene_botas_rojas": "True",
                    "tiene_cabello_pelirojo": "False",
                    "tiene_piel_azul": "False",
                    "tiene_un_guante_metalico": "False",
                    "tiene_corona": "False",
                    "tiene_cabello_blanco": "False",
                },
                "rey_elado": {
                    "tiene_gorra_blanca": "False",   
                    "tiene_mochila": "False",
                    "es_hombre": "True",
                    "tiene_cabello_rubio": "False",
                    "se_puede_estirar": "False",
                    "tiene_cabello_rosa": "False",
                    "tiene_vestido_rosa": "False",
                    "tiene_cabello_negro": "False",
                    "tiene_un_achagitarra": "False",
                    "tiene_botas_rojas": "False",
                    "tiene_cabello_pelirojo": "False",
                    "tiene_piel_azul": "True",
                    "tiene_un_guante_metalico": "False",
                    "tiene_corona": "True",
                    "tiene_cabello_blanco": "True",
                },
                "bily": {
                    "tiene_gorra_blanca": "False",   
                    "tiene_mochila": "False",
                    "es_hombre": "True",
                    "tiene_cabello_rubio": "False",
                    "se_puede_estirar": "False",
                    "tiene_cabello_rosa": "False",
                    "tiene_vestido_rosa": "False",
                    "tiene_cabello_negro": "False",
                    "tiene_un_achagitarra": "False",
                    "tiene_botas_rojas": "False",
                    "tiene_cabello_pelirojo": "True",
                    "tiene_piel_azul": "True",
                    "tiene_un_guante_metalico": "True",
                    "tiene_corona": "False",
                    "tiene_cabello_blanco": "False",
                }
            }

    def guardar_personajes(self):
        with open("personajes.json", "w") as file:
            json.dump(self.personajes, file, indent=4)

    def registrar_respuesta(self, respuesta):
        caracteristica = self.caracteristica_actual
        self.respuestas.append((caracteristica, respuesta))

        self.contador += 1

        if self.contador == len(self.caracteristicas):
            self.adivinar_personaje()
        else:
            self.caracteristica_actual = self.caracteristicas[self.contador]
            self.actualizar_pregunta()

    def adivinar_personaje(self):
        for personaje, caracteristicas in self.personajes.items():
            coincide = all(caracteristicas[caracteristica] == str(respuesta) for caracteristica, respuesta in self.respuestas)
            if coincide:
                self.personaje_adivinado = personaje
                break

        if self.personaje_adivinado is None:
            print("Ningún personaje coincide con las características.")
            nuevo_personaje = self.agregar_nuevo_personaje()
            if nuevo_personaje:
                self.personajes[nuevo_personaje] = {caracteristica: str(respuesta) for caracteristica, respuesta in self.respuestas}
                self.guardar_personajes()
                print(f"Se ha agregado el personaje {nuevo_personaje} al diccionario.")
        else:
            print(f"El personaje que estás pensando es {self.personaje_adivinado}")

        respuesta = messagebox.askyesno("Jugar de nuevo", f"Tu personaje es: {self.personaje_adivinado}\n¿Deseas jugar de nuevo?")
        if respuesta:
            self.reiniciar_juego()
        else:
            self.VenIm.destroy()
            self.master.destroy()

    def agregar_nuevo_personaje(self):
        nuevo_personaje = simpledialog.askstring("Nuevo Personaje", "Ningún personaje coincide. Ingresa un nuevo nombre:")
        return nuevo_personaje

    def reiniciar_juego(self):
        self.respuestas = []
        self.personaje_adivinado = None
        self.contador = 0
        self.caracteristicas = list(self.personajes["Rick"].keys())
        self.caracteristica_actual = self.caracteristicas[0]
        self.actualizar_pregunta()

    def actualizar_pregunta(self):
        caracteristica_formateada = self.caracteristica_actual.replace('_', ' ')
        self.lbl_preg.config(text=f"¿{caracteristica_formateada}?", font=("Arial Bold", 20), fg="Blue")
        

def iniciar_juego(venIm):
    ventana = tk.Tk()
    ventana.title("Adivina el Personaje")
    ventana.geometry("500x100+300+400")
    mi_ventana = MiVentana(ventana,venIm)
    ventana.mainloop()


    
    





class Ventana1_MostrarPers:
    def __init__(self, master):
        self.master = master

        #EtiquetasFranklin Gothic Book
        
        self.lbl_title = tk.Label(master, text="¡Bienvenido al juego Adivina Quién de Hora de Aventura!")
        self.lbl_title.config(font=("Franklin Gothic Book", 20))
        self.lbl_title.config(fg="black")
        self.lbl_title.place(x=180,y=10)
        
        self.lbl_title2 = tk.Label(master, text="Elige tu personaje")
        self.lbl_title2.config(font=("Franklin Gothic Book", 16))
        self.lbl_title2.config(fg="blue")
        self.lbl_title2.place(x=400,y=60)
        
        
        #Imagenes
        
        img_Rick = Image.open("finn.jpeg")  
        img_Rick_tk = ImageTk.PhotoImage(img_Rick)
        self.lbl_img_Rick = tk.Label(master, image=img_Rick_tk)
        self.lbl_img_Rick.image = img_Rick_tk
        self.lbl_img_Rick.pack()
        self.lbl_img_Rick.place(x=70,y=100)
        
        img_Morthy = Image.open("jake.jpg")  
        img_Morthy_tk = ImageTk.PhotoImage(img_Morthy)
        self.lbl_img_Morthy = tk.Label(master, image=img_Morthy_tk)
        self.lbl_img_Morthy.image = img_Morthy_tk
        self.lbl_img_Morthy.pack()
        self.lbl_img_Morthy.place(x=400,y=100)
                    
        img_Summer = Image.open("dulce.jpg")  
        img_Summer_tk = ImageTk.PhotoImage(img_Summer)
        self.lbl_img_Summer = tk.Label(master, image=img_Summer_tk)
        self.lbl_img_Summer.image = img_Summer_tk
        self.lbl_img_Summer.pack()
        self.lbl_img_Summer.place(x=700,y=100)
        
        img_Beth = Image.open("marc.jpg")  
        img_Beth_tk = ImageTk.PhotoImage(img_Beth)
        self.lbl_img_Beth = tk.Label(master, image=img_Beth_tk)
        self.lbl_img_Beth.image = img_Beth_tk
        self.lbl_img_Beth.pack()
        self.lbl_img_Beth.place(x=110-50,y=310+50)
        
        img_Jerry = Image.open("rey.jpg")  
        img_Jerry_tk = ImageTk.PhotoImage(img_Jerry)
        self.lbl_img_Jerry = tk.Label(master, image=img_Jerry_tk)
        self.lbl_img_Jerry.image = img_Jerry_tk
        self.lbl_img_Jerry.pack()
        self.lbl_img_Jerry.place(x=400-50,y=300+50)
        
        img_Jessica = Image.open("byli.jpg")  
        img_Jessica_tk = ImageTk.PhotoImage(img_Jessica)
        self.lbl_img_Jessica = tk.Label(master, image=img_Jessica_tk)
        self.lbl_img_Jessica.image = img_Jessica_tk
        self.lbl_img_Jessica.pack()
        self.lbl_img_Jessica.place(x=670-50,y=330+50)
        
        #Botones
        
        self.boton_cerrar = tk.Button(master, text="Siguiente", command=self.cerrar_ventana)
        self.boton_cerrar.config(font=("Arial", 20))
        self.boton_cerrar.config(bg="red", fg="black")
        self.boton_cerrar.place(x= 800, y = 500)

    def cerrar_ventana(self):
        self.master.destroy()
        nueva_ventana = Ventana2_RondaPreg()

class Ventana2_RondaPreg:
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry("1250x350+150+10")
        self.master.title("Ronda de preguntas")
        
        #Imagenes
        
        img_Rick = Image.open("finn.jpeg")  
        img_Rick_tk = ImageTk.PhotoImage(img_Rick)
        self.lbl_img_Rick = tk.Label(self.master, image=img_Rick_tk)
        self.lbl_img_Rick.image = img_Rick_tk
        self.lbl_img_Rick.pack()
        self.lbl_img_Rick.place(x=48,y=38)
        
        img_Morthy = Image.open("jake.jpg")  
        img_Morthy_tk = ImageTk.PhotoImage(img_Morthy)
        self.lbl_img_Morthy = tk.Label(self.master, image=img_Morthy_tk)
        self.lbl_img_Morthy.image = img_Morthy_tk
        self.lbl_img_Morthy.pack()
        self.lbl_img_Morthy.place(x=250,y=38)
                    
        img_Summer = Image.open("dulce.jpg")  
        img_Summer_tk = ImageTk.PhotoImage(img_Summer)
        self.lbl_img_Summer = tk.Label(self.master, image=img_Summer_tk)
        self.lbl_img_Summer.image = img_Summer_tk
        self.lbl_img_Summer.pack()
        self.lbl_img_Summer.place(x=430,y=38)
        
        img_Beth = Image.open("marc.jpg")  
        img_Beth_tk = ImageTk.PhotoImage(img_Beth)
        self.lbl_img_Beth = tk.Label(self.master, image=img_Beth_tk)
        self.lbl_img_Beth.image = img_Beth_tk
        self.lbl_img_Beth.pack()
        self.lbl_img_Beth.place(x=600,y=38)
        
        img_Jerry = Image.open("rey.jpg")  
        img_Jerry_tk = ImageTk.PhotoImage(img_Jerry)
        self.lbl_img_Jerry = tk.Label(self.master, image=img_Jerry_tk)
        self.lbl_img_Jerry.image = img_Jerry_tk
        self.lbl_img_Jerry.pack()
        self.lbl_img_Jerry.place(x=800,y=38)
        
        img_Jessica = Image.open("byli.jpg")  
        img_Jessica_tk = ImageTk.PhotoImage(img_Jessica)
        self.lbl_img_Jessica = tk.Label(self.master, image=img_Jessica_tk)
        self.lbl_img_Jessica.image = img_Jessica_tk
        self.lbl_img_Jessica.pack()
        self.lbl_img_Jessica.place(x=1050,y=38)
        
        #Etiquetas
        
        self.lbl_tPers = tk.Label(self.master, text="Personajes")
        self.lbl_tPers.config(font=("Arial Bold", 20))
        self.lbl_tPers.config(fg="green")
        self.lbl_tPers.pack()
        
        
        
        iniciar_juego(self.master)   
        
        self.master.mainloop()
    
    def cerrar_ventana(self):
        self.master.destroy()
        

    

if __name__ == "__main__":
    
    # Crear la ventana inicio
    ventana_inicio = tk.Tk()
    ventana_inicio.geometry("1000x650+150+10")
    ventana_inicio.title("Personajes")
 

    # Crear una instancia de VentanaAnterior
    ventana = Ventana1_MostrarPers(ventana_inicio)

    ventana_inicio.mainloop()

    





    

